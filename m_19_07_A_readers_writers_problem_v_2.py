import threading


class ReaderWriter:
    """
    `LR` and `LW` serve as read and write locks.

    `read_count` tracks the # of readers.

    [
    `data` stands for a "shared object",
    i.e. an object that many threads are expected to read from and write to
    ]
    """

    LR = threading.Condition()
    LW = threading.Condition()

    read_count = 0

    data = 0


class Reader(threading.Thread):
    def run(self):
        while True:
            # Guarantee that
            # any writer [thread], which acquires `Shared.write_cv`,
            # will be scheduled ahead by all subsequent reader[ thread]s.
            with ReaderWriter.LW:
                pass

            with ReaderWriter.LR:
                ReaderWriter.read_count += 1

            # Read the shared object.
            print(ReaderWriter.data)

            with ReaderWriter.LR:
                ReaderWriter.read_count -= 1
                ReaderWriter.LR.notify()

            do_something_else()


class Writer(threading.Thread):
    def run(self):
        while True:
            with ReaderWriter.LW:
                done = False

                while not done:
                    with ReaderWriter.LR:
                        if ReaderWriter.read_count == 0:
                            # Write to the shared object.
                            ReaderWriter.data += 1
                            done = True
                        else:
                            # Use `wait`/`notify` to avoid busy waiting.
                            while ReaderWriter.read_count != 0:
                                ReaderWriter.LR.wait()

            do_something_else()
