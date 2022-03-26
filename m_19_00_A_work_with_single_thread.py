"""
Key points:

    - `threading.Thread` represents an activity
      that is run in a separate thread of control

    - there are two categories of `threading.Thread`s:
      one that are daemonic + ones that are not daemonic

    - a "daemonic thread" does not mean the same as a "background thread":
      a "background thread" refers to any `thread.Thread`;
      a "daemonic thread" is 1 of the 2 possible categories of "background threads";
      (a "separate thread" is the same as a "background thread";)

    - if you create and start multiple `threading.Thread`s',
      it is the operating system that schedules/decides
      when each of the multiple threads is allowed to execute its next statement
      (
      for more information on this point,
      please study the next module carefully
      )
"""


import logging
import threading
import time


def fake_do_slow_computation(thread_name: str) -> None:
    """
    (
    This is intended to be run
    only from within a background thread.
    )
    """
    logging.info(f"[thread {thread_name}] starting")

    time.sleep(2)

    logging.info(f"[thread {thread_name}] finishing")


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    logging.info("[main thread] starting")
    background_thread_name: str = "1"
    # fmt: off
    '''
    In computer science, a "daemon" is a process that runs in the background.

    Python's `threading` module has a more specific meaning for "daemon".
    [
    In a nutshell, every `threading.Thread` is either daemonic or not daemonic.
    The different between those two categories of `threading.Thread`s is as follows:
    ]

        If a program is running `Thread`s that are not [daemonic],
        then the program will wait for those threads to complete before it terminates.

        `Thread`s that are [daemonic], however, [are abruptly stopped] wherever they are
        when the program [exits].
    
    (
    A daemon thread will shut down immediately when the program exits.
    One [reasonable working definition of a] daemon thread [is] a thread that
    (a) runs in the background and
    (b) [that you don't have to remember to shut down].
    )
    '''
    # fmt: on

    logging.info(f"[main thread] creating 'thread {background_thread_name}'")
    t = threading.Thread(
        target=fake_do_slow_computation,
        args=(background_thread_name,),
    )

    logging.info(f"[main thread] starting 'thread {background_thread_name}'")
    t.start()

    logging.info(f"[main thread] wait for 'thread {background_thread_name}' to finish")
    # fmt: off
    '''
    The following statement causes
    the calling thread, which in this case is the 'main thread', to wait
    until `t` has terminated.

    (
    Including the following statement
    (a) doesn't make any difference if the thread `t` is not daemonic, but
    (b) does make a difference if the thread `t` is daemonic.
    )
    '''
    # fmt: on
    # t.join()

    logging.info("[main thread] finishing")
