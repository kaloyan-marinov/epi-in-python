"""
Key points:

    - one of the more difficult issues you'll run into when writing threaded programs
      if _race conditions_

    - in this module, we are going to provide
      a artificial but easy-to-understand example with a race condition:

        [background] threads [are going to]
        [access] a single shared object [in an interleaving manner],
        [which will cause the threads to overwrite] each other's results

    - why is the example, which is provided in this module, described as "artificial"?

        Because, by making an artificial call to `time.sleep()`,
        the example achieves determinism with regard to
        when and how frequently a race condition actually occurs
        - namely, a race condition occurs each and every time this module is run.

        By contrast,
        most race conditions [that occur in practice] (lack determinism with regard to
        when and how frequently they actually occur; as a consequence, they)
        are [much less] obvious.
        Frequently, they only occur rarely, and they can produce confusing results.
        As you can imagine, this makes them quite difficult to debug.

        For a more realistic example with a race condition,
        please study the next module carefully.

    - in addition to the situation
      when two or more threads access a shared piece of data or resource,
      here are some more examples of situations, in which race conditions can occur:
      
        when one thread frees memory or closes a file handle
        before the other thread is finished accessing it
"""

import concurrent.futures
import logging
import time


class FakeDatabase:
    """
    This keeps track of a single integer.
    """

    def __init__(self) -> None:
        self.value: int = 0

    def update(self, background_thread_name: str) -> None:
        """
        (
        This is intended to be called
        only from within a background thread.
        )

        Simulate:
            - reading from [the] database;
            - doing some computation on the read data;
            - and writing the computed value back to the database
        """
        logging.info(
            f"[thread {background_thread_name}] is starting to update `self.value`"
        )

        # Simulate reading from [the] database.
        local_copy = self.value

        # Simulate [doing some computation on the read data]
        # and writing the computed value back to the database.
        local_copy += 1

        # fmt: off
        '''
        Swapping the order of the previous statement and the following one
        doesn't change the result of running this module.

        However, it is my view that swapping those statements would advance closer to
        modeling a realistic situation
        (such as one, in which `time.sleep(0.1)` corresponds to
        the function issuing an HTTP request and waiting for a response to arrive.).
        '''
        # fmt: on
        time.sleep(0.1)

        self.value = local_copy

        logging.info(
            f"[thread {background_thread_name}] has finished updating `self.value`"
        )


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    logging.info("[main thread] starting")
    fake_db = FakeDatabase()

    logging.info(f"[main thread] fake_db.value={fake_db.value}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # fmt: off
        '''
        Each thread is going to have a reference to the same `FakeDatabase` object,
        [namely to] `fake_db`.

            When [each] thread starts executing `.update()`,
            it has its own version of all of the data _local_ to the function.
            (
            [That] means that all variables that are scoped (or local) to [the] function
            are _thread-safe_.
            )
        '''
        # fmt: on
        for i in range(2):
            background_thread_name = str(i)
            executor.submit(fake_db.update, background_thread_name)

    logging.info(f"[main thread] fake_db.value={fake_db.value}")  # 1

    logging.info(f"[main thread] finishing")
