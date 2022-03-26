import threading


class Shared:
    """
    `read_cv` and `write_cv` serve as read and write locks.

    `n_reader_threads` tracks the # of reader[ thread]s.

    [
    `data` stands for a "shared object",
    i.e. an object that many threads are expected to read from and write to
    ]
    """

    read_cv = threading.Condition()
    write_cv = threading.Condition()

    n_reader_threads = 0

    data = 0


def read_from_data_in_Shared():
    while True:
        # Guarantee that
        # any writer [thread], which acquires `Shared.write_cv`,
        # will be scheduled ahead by all subsequent reader[ thread]s.
        with Shared.write_cv:
            pass

        with Shared.read_cv:
            Shared.n_reader_threads += 1

        # Read the shared object.
        print(Shared.data)

        with Shared.read_cv:
            Shared.n_reader_threads -= 1
            Shared.read_cv.notify()

        do_something_else()


def write_to_data_in_Shared(self):
    while True:
        with Shared.write_cv:
            done = False

            while not done:
                with Shared.read_cv:
                    if Shared.n_reader_threads == 0:
                        # Write to the shared object.
                        Shared.data += 1
                        done = True
                    else:
                        # Use `wait`/`notify` to avoid busy waiting.
                        while Shared.n_reader_threads != 0:
                            Shared.read_cv.wait()

        do_something_else()


if __name__ == "__main__":

    reader = threading.Thread(target=read_from_data_in_Shared)
    writer = threading.Thread(target=write_to_data_in_Shared)

    reader.start()
    writer.start()

    reader.join()
    writer.join()
