"""
In spirit,
this module is equivalent to `m_19_08_*.py`.

But, in my opinion,
this module matches (the description of) the official solution
more closely than `m_19_08_*.py` does.

TODO: clean up this module by
      - removing unnecessary comments
      - ensuring that all existing docstrings are up-to-date
      - adding missing docstrings
      - trying to eliminate `cv = self._cv` (and its 2 "sibling" statements)
"""

import datetime
import functools
import heapq
import logging
import threading
from typing import Dict, List


logger = logging.getLogger(__name__)
logger.addHandler(
    logging.NullHandler(),
)


@functools.total_ordering  # Python docs: "In addition, the class should supply an `__eq__()` method.""
class Task:
    """
    This models a task,
    which has to be launched
          (:= consists in starting to execute a given function)
    at a specified time in the future.
    """

    def __init__(
        self,
        task_id: str,
        fn,
        launch_time: datetime.datetime,
    ) -> None:  # Type for `fn`?
        self.id: str = task_id
        self.fn = fn
        self.launch_time: datetime.datetime = launch_time
        self.cancelled: bool = False

    def __le__(self, other: "Task") -> bool:
        """
        Compare 2 instances based on their `launch_time` times.
        """
        return self.launch_time <= other.launch_time

    @property
    def time_in_seconds_until_launch(self) -> float:
        """
        Return the remaining time (in seconds)
        before (the task modeled by) `self` has to be launched.
        """
        return (self.launch_time - datetime.datetime.now()).total_seconds()

    # fmt: off
    '''
    def cancel(self) -> None:
        """
        Cancel (the task modeled by) `self`
        if it has not already been launched.
        """
        self.cancelled = True
        logger.info("cancelled %s", self)
        # In my view,
        # this method's implementation introduces a strange coupling btwn both classes;
        # it should be possible to avoid that by
        # (a) moving `cancel` out of `Task` and into `SchedulerForDeferredTasks`,
        # (b) requiring each `Task` to have a unique ID/name,
        # (c) making `SchedulerForDeferredTasks` maintain also a "`task_id_2_min_heap_entry`" (as recommended by the book), and
        # (d) replacing `Task` with
        #   ```
        #   class Task(typing.NamedTuple):
        #       id: str
        #       fn: typing.Any  # What would be a more suitable annotation?
        #       launch_time: datetime.datetime
        #       # cancelled: bool  # I'm not yet sure whether there's an easy way of eliminating this altogether.
        #
        #       def __eq__(self, other: "Task") -> bool:
        #           return self.id == other.id
        #
        #       @property
        #       def time_in_seconds_until_launch(self) -> float:
        #           return (self.launch_time - datetime.datetime.now()).total_seconds()
        #
        #       @functools.total_ordering
        #       def __le__(self, other: "Task") -> bool:
        #           return self.launch_time <= other.launch_time
        #   ```
    '''
    # fmt: on


class SchedulerForDeferredTasks:
    """
    This class manages/maintains a schedule of `Task`s, each of which is to be
    launched in a background thread at a specified time in the future.

    Call the `schedule` method to schedule a task to be launched at a particular time;
    the `schedule` method returns a `Task` object representing the scheduled task.

    The ability to cancel a `Task` is provided by `Task.cancel()`
    - see the docstring of that method.
    """

    def __init__(self):
        self._cv = threading.Condition(lock=threading.Lock())

        self._tasks: List[Task] = []
        self._task_id_2_task: Dict[str, Task] = {}

        cv = self._cv

        tasks = self._tasks
        task_id_2_task = self._task_id_2_task

        def _manage_schedule_of_tasks():
            while True:

                # Determine which one of the `tasks` has the soonest `launch_time`,
                # and wait either (a) until that time, or (b) the thread executing this
                # function is notified (of a new `Task` having been scheduled) - whichever
                # comes first.
                with cv:

                    while True:

                        seconds_till_soonest_launch = None

                        while tasks and tasks[0].cancelled:
                            t: Task = heapq.heappop(tasks)
                            del task_id_2_task[t.id]

                        if tasks:
                            seconds_till_soonest_launch = tasks[
                                0
                            ].time_in_seconds_until_launch
                            if seconds_till_soonest_launch <= 0:
                                task = heapq.heappop(tasks)
                                del task_id_2_task[task.id]
                                break

                        cv.wait(timeout=seconds_till_soonest_launch)

                # Start the determined Task.
                logger.info("starting task %s", task)
                threading.Thread(target=task.fn).start()

        threading.Thread(
            target=_manage_schedule_of_tasks,
            name="_manage_schedule_of_tasks",
        ).start()

    def schedule(self, task_id: str, fn, launch_time: datetime.datetime) -> None:
        """
        Schedule a `Task` that will start executing `fn` at or after `launch_time`,
        and return an object representing that `Task`.
        """
        task = Task(task_id, fn, launch_time)

        logger.info("scheduling task %s", task)
        with self._cv:
            heapq.heappush(self._tasks, task)
            self._task_id_2_task[task.id] = task
            self._cv.notify()

        logger.info("scheduled task %s", task)

    def cancel(self, task_id: str) -> bool:
        if task_id not in self._task_id_2_task:
            return False

        t: Task = self._task_id_2_task[task_id]
        t.cancelled = True

        logger.info("cancelled %s", t)

        return True


def main():
    import time

    logging.basicConfig(level=logging.INFO, format="%(threadName)-10s: %(message)s")

    datetime_now_1 = datetime.datetime.now()

    def mock_perform_task():
        logger.info(
            "running, elapsed: %s",
            (datetime.datetime.now() - datetime_now_1).total_seconds(),
        )

    scheduler = SchedulerForDeferredTasks()

    scheduler.schedule(
        "task_1",
        mock_perform_task,
        datetime_now_1 + datetime.timedelta(seconds=1),
    )

    scheduler.schedule(
        "task_2",
        mock_perform_task,
        datetime_now_1 + datetime.timedelta(seconds=2),
    )
    scheduler.cancel("task_2")

    # Note that,
    # despite the order
    # in which the client (= this function) schedules `task_3` and `task_4`,
    # `task_4.launch_time` is sooner than `task_3.launch_time`.
    scheduler.schedule(
        "task_3",
        mock_perform_task,
        datetime_now_1 + datetime.timedelta(seconds=3),
    )

    scheduler.schedule(
        "task_4",
        mock_perform_task,
        datetime_now_1 + datetime.timedelta(seconds=2.5),
    )

    # Make the client (= this function) sleep for a bit,
    # and then schedule a `task_5`, `task_6`, and `task_7`
    # (but do note that
    # `task_7.launch_time` is sooner than `task_6.launch_time`,
    # which itself is sooner than `task_5.launch_time`).
    time.sleep(5)

    datetime_now_2 = datetime.datetime.now()

    scheduler.schedule(
        "task_5",
        mock_perform_task,  # Originally was `functools.partial(mock_perform_task)`, but doesn't seem to be needed.
        datetime_now_2 + datetime.timedelta(seconds=5),
    )

    scheduler.schedule(
        "task_6",
        mock_perform_task,
        datetime_now_2 + datetime.timedelta(seconds=4),
    )

    scheduler.schedule(
        "task_7",
        mock_perform_task,
        datetime_now_2 + datetime.timedelta(seconds=3.5),
    )


if __name__ == "__main__":
    main()
