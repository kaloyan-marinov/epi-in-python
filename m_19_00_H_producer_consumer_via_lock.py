"""
Key points:

    - The Producer-Consumer Problem is a standard computer science problem
      used to look at threading or process synchronization issues.
    
    - For this example:

        - Imagine a program that needs to read messages from a network and write them to
          disk.

          The program does not request a message when it wants. It must be listening
          and accept messages as they come in. The messages will not come in at a
          regular pace, but will be coming in bursts.
          
          This part of the program is called _the producer_.

        - On the other side,
          once you have a message, you need to write it to a database.
          
          The database access is slow,
          but fast enough to keep up to the average pace of messages.
          It is not fast enough to keep up when a burst of messages comes in.
          
          This part is _the consumer_.

        - In between the producer and the consumer,
          there will be a `Pipeline` that ...

    - This module contains a solution of the Producer-Consumer Problem,
      which uses a `threading.Lock`.
      
        - It is a working solution;
          also, it uses the only one of Python's synchronization primitives
          that we have seen so far.
        
        - But it does have a shortcoming:
          it only allows a single value in the pipeline at a time.
          [
          In other words,
          the `Pipeline` does not support (= cannot be used by) any "producer"
          that gets[/generates/becomes ready to send?] a burst of messages.
          ]
"""

import concurrent.futures
import logging
import random
import threading


SENTINEL = object()


class Pipeline:
    """
    [This models a pipeline between a producer and a consumer
    with a capacity of a single element.]
    """

    def __init__(self) -> None:
        self._message = 0

        # fmt: off
        '''
        To synchronize/coordinate
        the producer's access and the consumer's access to the shared `self.message`,
        this class will use two `threading.Lock` instances:

            - the "producer lock" will be used
              to restrict the producer (thread)'s access to the message;

            - the "consumer lock" will be used
              to restrict the consumer (thread)'s access to the message;
        '''
        # fmt: on
        self._producer_lock = threading.Lock()
        self._consumer_lock = threading.Lock()

        # fmt: off
        '''
        [The following] is the state you want to start in:
            
            The producer is allowed to add a new message,
            but the consumer needs to wait until a message is present.
        
        That means:

            - the "producer lock" should be in its unlocked state
                                            (= released),
              which it is (because, whenever a lock is created,
              it is created in its unlocked state);
            
            - the "consumer lock" should be in its locked state
                                            (= acquired).
        '''
        # fmt: on
        self._consumer_lock.acquire()

    def send_message(self, message: str, name: str) -> None:
        self._producer_lock.acquire()

        self.message = message

        self._consumer_lock.release()

    def receive_message(self, name: str) -> None:
        """
        There's something subtle [in this method's implementation]
        that is important but also pretty easy to miss
        - namely, the fact that it doesn't just `return self.message`!
        (
        If it did just `return self.message`,
        that would open up room for race conditions to occur.
        )
        """
        self._consumer_lock.acquire()

        message = self.message

        self._producer_lock.release()

        return message


def producer(pipeline: Pipeline) -> None:
    """
    Pretend we're getting a message from the network.
    [or rather: "sending a message over the network"?]
    """
    for _ in range(10):
        # (Simulate the) Generation of a real message.
        message = random.randint(1, 100)

        # Send the message into the `pipeline` (for the consumer to receive later).
        logging.info(f"[producer] preparing to send the following message: {message}")
        pipeline.send_message(message, "Producer")

    # Send a "sentinel message" to tell the consumer we're done.
    pipeline.send_message(SENTINEL, "Producer")


def consumer(pipeline: Pipeline) -> None:
    """
    Pretend we're saving a message in [some] database.
    [or rather: "receiving a message over the network"?]
    """
    message = 0
    while message is not SENTINEL:
        # Receive a message from the `pipeline`.
        message = pipeline.receive_message("Consumer")

        # (Simulate the) Saving of the message to [some] database.
        if message is not SENTINEL:
            logging.info(
                f"[consumer] received and storing the following message: {message}"
            )


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
