import datetime
import functools
import heapq
import logging
import threading
from typing import List


logger = logging.getLogger(__name__)
logger.addHandler(
    logging.NullHandler(),
)


class SchedulerForDeferredTasks:
    """
    This class manages/maintains a schedule of tasks, each of which is to be
    launched in a background thread at a specified time in the future.

    Call the `schedule` method to schedule a task to be launched at a particular time;
    the `schedule` method returns an object representing the scheduled task.

    Call the task( object)'s `cancel` method to cancel it
    if it has not already been launched.
    """

    @functools.total_ordering  # Python docs: "In addition, the class should supply an `__eq__()` method.""
    class _Task:
        """
        This models a task,
        which consists in starting to execute a given function (=: will be launched)
        at a specified time in the future.
        """

        def __init__(self, fn, launch_time: datetime.datetime) -> None:
            self.fn = fn
            self.launch_time: datetime.datetime = launch_time
            self.cancelled: bool = False

        def __le__(self, other: "_Task") -> bool:
            # Tasks compare according to their launch_time time.
            return self.launch_time <= other.launch_time

        @property
        def time_in_seconds_until_launch(self) -> int:
            """
            Return the remaining time (in seconds)
            before `self` has to be launched.
            """
            return (self.launch_time - datetime.datetime.now()).total_seconds()

        def cancel(self) -> None:
            """
            Cancel (the task represented by) `self`
            if it has not already been launched.
            """
            self.cancelled = True
            logger.info("cancelled %s", self)

    def __init__(self):
        self._cv = threading.Condition(threading.Lock())

        self._tasks: List[_Task] = []

        cv = self._cv
        tasks = self._tasks

        def run():
            while True:

                # Determine which one of the `tasks` has the soonest `launch_time`,
                # and wait either (a) until that time, or (b) the thread executing this
                # function is notified (of a new task having been scheduled) - whichever
                # comes first.
                with cv:

                    while True:

                        seconds_till_soonest_launch = None

                        while tasks and tasks[0].cancelled:
                            heapq.heappop(tasks)

                        if tasks:
                            seconds_till_soonest_launch = tasks[
                                0
                            ].time_in_seconds_until_launch
                            if seconds_till_soonest_launch <= 0:
                                task = heapq.heappop(tasks)
                                break

                        cv.wait(timeout=seconds_till_soonest_launch)

                # Start the determined `Task`.
                logger.info("starting task %s", task)
                threading.Thread(target=task.fn).start()

        threading.Thread(target=run, name="SchedulerForDeferredTasks").start()

    def schedule(
        self, fn, launch_time: datetime.datetime
    ) -> _Task:  # Suggests that `_Task` should not be a private class.
        """
        Schedule a `_Task` that will start executing `fn` at or after `launch_time`,
        and return an object representing that `_Task`.
        """
        task = self._Task(fn, launch_time)

        logger.info("scheduling task %s", task)
        with self._cv:
            heapq.heappush(self._tasks, task)
            self._cv.notify()

        logger.info("scheduled task %s", task)
        return task


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

    task_1 = scheduler.schedule(
        mock_perform_task,
        datetime_now_1 + datetime.timedelta(seconds=1),
    )

    task_2 = scheduler.schedule(
        mock_perform_task,
        datetime_now_1 + datetime.timedelta(seconds=2),
    )
    task_2.cancel()

    # Note that,
    # despite the order
    # in which the client (= this function) schedules `task_3` and `task_4`,
    # `task_4.launch_time` is sooner than `task_3.launch_time`.
    task_3 = scheduler.schedule(
        mock_perform_task,
        datetime_now_1 + datetime.timedelta(seconds=3),
    )

    task_4 = scheduler.schedule(
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

    task_5 = scheduler.schedule(
        mock_perform_task,  # Originally was `functools.partial(mock_perform_task)`, but doesn't seem to be needed.
        datetime_now_2 + datetime.timedelta(seconds=5),
    )

    task_6 = scheduler.schedule(
        mock_perform_task,
        datetime_now_2 + datetime.timedelta(seconds=4),
    )

    task_7 = scheduler.schedule(
        mock_perform_task,
        datetime_now_2 + datetime.timedelta(seconds=3.5),
    )


if __name__ == "__main__":
    main()
