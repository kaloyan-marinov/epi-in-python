"""
Key points:

    - in this module, we are going to provide
      a more-realistic-than-the-example-in-the-previous-module example
      with a race condition

        [analogously to the example in the previous module,]
        [background] threads [are going to]
        [access] a single shared object [in an interleaving manner],
        [which will cause the threads to overwrite] each other's results

        [unlike the example in the previous module,]
        this module's example:

            (a) will not (have to) make any artificial calls to `time.sleep()`

            (b) lacks determinism with respect to
                when and how frequently race conditions occur,
                which in turn causes
                the results of running this module
                to be non-deterministic

    - to become able to reason about
      why and where race conditions can occur in this module's example,
      [we have to (first be supplied with and
      to then relentlessly/ceaselessly) bear] in mind
      the following two facts:

        1. Even an operation like `x += 1` takes the processor many steps.
           Each of these steps is a separate instruction to the processor.

           ```
            >>> def inc(x):
            ...    x += 1
            ...
            >>> import dis
            >>> dis.dis(inc)
            2           0 LOAD_FAST                0 (x)
                        2 LOAD_CONST               1 (1)
                        4 INPLACE_ADD
                        6 STORE_FAST               0 (x)
                        8 LOAD_CONST               0 (None)
                        10 RETURN_VALUE
           ```

        2. The operating system can swap which thread is running _at any time_.
           A thread can be swapped out after any of these small processor instructions.
           This means that
           a thread can be put to sleep
           to let another thread run
           in the _middle_ of a Python statement.
    
    - Pause briefly
      to tie in the facts about processor instructions
      with the previous module's example.
      
        That example's `.update()` is also a listing of separate processor instructions;
        that listing contains a transition,
        which is equivalent to the transition
        between processor instructions marked with 4 and 6
        within the listing displayed above.

        It is entirely possible that,
            every once in while,
            the operating system would switch threads at that exact point
            even without the `time.sleep(0.1)` call;
        but,
            with that call in place,
            the operating system will switch threads (at that exact point)
            every single time.

    - Last but not least,
      tie in the facts about processor instructions
      with this module's example.

        This example's `.update()` is also contains a transition,
        which is equivalent to the transition mentioned above.
        
        Although this example doesn't make any calls to `time.sleep`,
        we already learned that
        the operating system could swap out the running thread at any point.
        To fix ideas, let A refer to the running thread (at some fixed time instant);
        if the operating system swaps out A
        and runs a different thread that also modifies the shared object,
        then, when thread A resumes,
        it will overwrite the shared object with a[ stale and thus] incorrect value.
"""

import concurrent.futures
import logging


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

        for _ in range(10 ** 6):
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

        for i in range(2):
            background_thread_name = str(i)
            future = executor.submit(fake_db.update, background_thread_name)
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
