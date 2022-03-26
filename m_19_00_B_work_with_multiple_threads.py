"""
Key points:

    - the following was already stated in the preceding module:
      if you create and start multiple `threading.Thread`s',
      the order in which the threads' [individual statements] are run:

      (a) is determined by the operating system;

      (b) can be quite hard[ or, more precisely, practically impossible] to predict;

      (c) may (and likely will) vary from run to run
          (you need to be aware of that when you design algorithms that use `threading`)

    - the preceding point is demonstrated by the fact that
      running this module several times
      will cause its logging statements to be executed in different orders

    - pretty much the only non-trivial thing we can say with any degree of certainty is
      the following:
      if we run this module several times,
      then the "[main thread] joining 'thread 0'" log statement will be executed
      about 2 seconds before
      its "[main thread] joining 'thread 1'"
      and "[main thread] joining 'thread 2'" counterparts

    - assuming you have to write a program that creates and starts multiple threads,
      the Python Standard Library provides several "synchronization primitives"
      that can be utilized to guarantee determinism in the order,
      in which the different threads get executed
      (
      for more information on this point,
      please study the module after the next one carefully
      )
"""

import logging
import threading

from typing import List

from m_19_00_A_work_with_single_thread import fake_do_slow_computation


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    logging.info("[main thread] starting")

    threads: List[threading.Thread] = []
    for i in range(3):
        background_thread_name = str(i)

        logging.info(f"[main thread] creating 'thread {background_thread_name}'")
        t = threading.Thread(
            target=fake_do_slow_computation,
            args=(background_thread_name,),
        )

        threads.append(t)

        logging.info(f"[main thread] starting 'thread {background_thread_name}'")
        t.start()

    for i, t_i in enumerate(threads):
        name_of_t_i: str = str(i)

        logging.info(f"[main thread] joining 'thread {name_of_t_i}'")
        t.join()

        logging.info(f"[main thread] right after joining 'thread {name_of_t_i}'")

    logging.info("[main thread] finishing")
