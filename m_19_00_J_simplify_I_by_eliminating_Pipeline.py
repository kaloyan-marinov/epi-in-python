"""
Key points:

    - This module contains a solution of the Producer-Consumer Problem,
      which:

        overcomes the shortcoming of the solution, which is part of the previous module
        (
        = uses a `queue.Queue` instance directly,
          instead of first implementing a _very_ simple subclass of `queue.Queue`
          and only then using an instance of that subclass
        );
      
        uses a `queue.Queue` and `threading.Event`;

    - This module, as well as the following paragraph from the official documentation of
      the `queue` module, strongly suggests that
      the `queue.Queue` class is provided (= put forward) by Python Standard Library
      as a standard, go-to solution _precisely_ of the Producer-Consumer Problem.
"""


import concurrent.futures
import logging
import queue
import random
import threading
import time


def producer(queue: queue.Queue, event: threading.Event) -> None:
    """
    Pretend we're getting a message from the network.
    [or rather: "sending a message over the network"?]
    """
    while not event.is_set():
        # (Simulate the) Generation of a real message.
        message = random.randint(1, 100)

        # Send the message into the `queue` (for the consumer to receive later).
        logging.info(f"[producer] preparing to send the following message: {message}")
        queue.put(message)

    logging.info("[producer] received event - exiting")


def consumer(queue: queue.Queue, event: threading.Event) -> None:
    """
    Pretend we're saving a message in [some] database.
    [or rather: "receiving a message over the network"?]

    NB: The 2nd part of the condition in the `while` loop is strictly necessary!
        (
        Without it, there are two bad thing that can happen.

            The first is that you lose those final messages,

            but the more serious one is that
            the `producer` can get caught attempting to add a message to a full queue
            and never return.
        )
    """
    while not event.is_set() or not queue.empty():
        # Receive a message from the `queue`.
        message = queue.get()

        # (Simulate the) Saving of the message to [some] database.
        logging.info(
            f"[consumer] received and storing the following message: {message}"
            + f" (queue size: {queue.qsize()})"
        )

    logging.info("[consumer] received event - exiting")


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    q = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, q, event)
        executor.submit(consumer, q, event)

        # It is instructive to try running this module
        # when the following statement is modified in a few ways:
        #   - comment out the next statement
        #   - decrease 0.1 to 0.01,
        #     which would make the logging output
        #     shorter but also "übersichtlicher" (= more graspable)
        time.sleep(0.1)

        logging.info("[main thread] about to issue `event.set()`")
        event.set()
