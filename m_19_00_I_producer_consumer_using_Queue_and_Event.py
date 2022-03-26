"""
Key points:

    - This module contains a solution of the Producer-Consumer Problem,
      which:

        overcomes the shortcoming of the solution, which is part of the previous module
        (
        = allows more than 1 value in the pipeline at a time,
          which in turn requires its pipeline to be based on
          a data structure that allows the number to grow and shrink
          as [messages "back up"] from the "producer"
        );
      
        uses a `queue.Queue` and `threading.Event`;

    - This module demonstrates a different way [of stopping] the [background] threads -
      namely, by using a `threading.Event` instance.

        The `threading.Event` object allows one thread to signal an `event`
        while many other threads can be waiting for that `event` [...]

        The key usage in this code is that
        (a) the threads that are waiting for the `event`
        do not necessarily need to stop what they are doing, but
        (b) they can just check the status of the [`event`] every once in a while.

        The triggering of the event can be many things.
        In this example,
        the main thread will simply `time.sleep` for a short time
        and then issue `event.set()` [...]

    - Last but not least,
      this module's solution of the Producer-Consumer Problem does have a shortcoming:
      it implements a `Pipeline` class [as a _very_ simple subclass of] `queue.Queue`.
"""


import concurrent.futures
import logging
import queue
import random
import threading
import time


class Pipeline(queue.Queue):
    """
    [This models a pipeline between a producer and a consumer
    with a capacity of 10 elements.]
    """

    def __init__(self) -> None:
        super().__init__(maxsize=10)

    def send_message(self, message: str, name: str) -> None:
        self.put(message)

    def receive_message(self, name: str) -> None:

        value = self.get()
        return value


def producer(pipeline: Pipeline, event: threading.Event) -> None:
    """
    Pretend we're getting a message from the network.
    [or rather: "sending a message over the network"?]
    """
    while not event.is_set():
        # (Simulate the) Generation of a real message.
        message = random.randint(1, 100)

        # Send the message into the `pipeline` (for the consumer to receive later).
        logging.info(f"[producer] preparing to send the following message: {message}")
        pipeline.send_message(message, "Producer")

    logging.info("[producer] received event - exiting")


def consumer(pipeline: Pipeline, event: threading.Event) -> None:
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
    while not event.is_set() or not pipeline.empty():
        # Receive a message from the `pipeline`.
        message = pipeline.receive_message("Consumer")

        # (Simulate the) Saving of the message to [some] database.
        logging.info(
            f"[consumer] received and storing the following message: {message}"
            + f" (queue size: {pipeline.qsize()})"
        )

    logging.info("[consumer] received event - exiting")


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        # It is instructive to try running this module
        # when the following statement is modified in a few ways:
        #   - comment out the next statement
        #   - decrease 0.1 to 0.01,
        #     which would make the logging output
        #     shorter but also "übersichtlicher" (= more graspable)
        time.sleep(0.1)

        logging.info("[main thread] about to issue `event.set()`")
        event.set()
