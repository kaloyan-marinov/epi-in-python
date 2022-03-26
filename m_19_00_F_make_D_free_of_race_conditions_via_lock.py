"""
Key points:

    - Python's `threading` module provides several _synchronization primitives_,
      which a multi-threaded program can utilize
      in order to prevent race conditions from occurring

    - to prevent race conditions from occurring when we run the `m_19_00_D_*.py` module,
      we need a way to ensure that,
        at any given time, only 1 thread will be allowed
        to execute the read-modify-write portion of the code
    
    - Python provides a synchronization primitive called `threading.Lock`,
      which can be used to ensure the desiredatum described in the previous bulletpoint

    - A `threading.Lock` is an object that acts like a hall pass.
      Only one thread at a time can `.acquire()` the `threading.Lock`.
      Any other thread that wants the `threading.Lock` must wait
      until the holder of the `threading.Lock` `.release()`s it.

      (
      If the `threading.Lock` is first `.acquire()`d by thread A
      and thread B attempts to `.acquire()` the same lock,
      thread B will block (= have to wait) until thread A `.release()`s the lock.

      There's an important point here.
      If thread A never `.release()`s the lock,
      your program will become stuck.
      Such a situation is called a _deadlock_.
      )

    - last but not least,
      let us say that this module modifies the `m_19_00_D_*.py` module
      so as to prevent race conditions from occurring
      (and that modification can be summarized as
      the introduction and appropriate utilization of a `threading.Lock` instance)

      (
      It's worth noting here that
      [whichever of the 2] thread[s is scheduled to run] `fake_db.update`
      will hold on to `fake_db._lock`
      until that same thread is completely finished updating the database.
      In this case, that means the thread will hold the `fake_db._lock`
      while it
        [reads],
        [increments],
        sleeps,
        and [...] writes the [incremented] value back to the database.
      )
"""

import concurrent.futures
import logging
import threading
import time


class FakeDatabase:
    """
    This keeps track of a single integer.
    """

    def __init__(self) -> None:
        self.value: int = 0
        self._lock: threading.Lock = threading.Lock()

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
            f"[thread {background_thread_name}] is starting"
            " (by attempting to acquire `self._lock`)"
        )
        with self._lock:
            logging.info(
                f"[thread {background_thread_name}] has acquired `self._lock` successfully"
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

            logging.info(f"[thread {background_thread_name}] is releasing `self._lock`")

        logging.info(f"[thread {background_thread_name}] is exiting")


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
