import concurrent.futures
import logging
import threading


class FakeDatabase:
    """
    This keeps track of a single integer.
    """

    def __init__(self) -> None:
        self.value: int = 0

    def update(
        self,
        background_thread_name: str,
        lock: threading.Lock,
    ) -> None:
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

        for _ in range(10 ** 6):
            with lock:
                self.value += 1

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
        future_2_input = {}

        common_lock = threading.Lock()

        for i in range(2):
            background_thread_name = str(i)
            future = executor.submit(
                fake_db.update,
                background_thread_name,
                common_lock,
            )
            future_2_input[future] = background_thread_name

        for f in concurrent.futures.as_completed(future_2_input):
            logging.info(
                "[main thread] the following `Future` instance has"
                " completed (= finished or been cancelled):"
                f" {repr(f)}"
            )

    # fmt: on
    """
    Every run will cause the following statement to print a different value!

    (
    It is instructive to know that
    there do exist some (albeit limited) guarantees about the the (range of) values
    that could be possibly be printed by the following statement;
    cf. the solution of Problem 19.2.
    )
    """
    # fmt: off
    logging.info(f"[main thread] fake_db.value={fake_db.value}")

    logging.info(f"[main thread] finishing")
