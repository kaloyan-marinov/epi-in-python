"""
Key points:

    - the easiest way to start up a group of threads is to
      (a) create a `ThreadPoolExecutor` instance and
      (b) use it as a context manager;
      part (b) manages both the creation and destruction of the pool of threads for you

    - The end of the `with` block
      causes the `ThreadPoolExecutor` to [call] `.join()`
      on each of the threads in the pool.
    
    - It is _strongly_ recommended that
      you use `ThreadPoolExecutor` as a context manager when you can
      so that you never forget to `.join()` the threads.

    - as in the previous module, notice that
      running this module several times
      will cause its logging statements to be executed in different orders
      [
      because the scheduling of threads
      is done by the operating system and
      does not follow a plan that's easy to figure out
      ]
"""


import concurrent.futures
import logging

from m_19_00_A_work_with_single_thread import fake_do_slow_computation


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    logging.info("[main thread] starting")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(
            fake_do_slow_computation,
            (str(i) for i in range(3)),
        )

    logging.info("[main thread] finishing")
