"""
This module is an example of using Python's `threading` module
to animate a (simple) loading indicator for a (long-running) CLI Python program.
"""

import itertools
import threading
import time
import sys


main_thread_has_finished = False

# The following works
# as if you have shifted your cursor to the beginning of the string or line.
CARRIAGE_RETURN = "\r"


def print_loading_indicator():
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        if main_thread_has_finished:
            break

        sys.stdout.write(CARRIAGE_RETURN + "loading " + c)
        sys.stdout.flush()

        time.sleep(0.1)

    # sys.stdout.write(CARRIAGE_RETURN + "done!" + "\n") # done!ng |
    sys.stdout.write(CARRIAGE_RETURN + "done!    " + "\n")  # done!


def do_sth_time_consuming():
    global main_thread_has_finished
    # fmt: off
    '''
    The above can be eliminated
    if the global variable and global constant are encapsulated into a "shared" namespace like so:

    ```
    class Shared:
        main_thread_has_finished = False

        # The following works
        # as if you have shifted your cursor to the beginning of the string or line.
        CARRIAGE_RETURN = "\r"
    ```
    '''
    # fmt: on

    time.sleep(10)
    main_thread_has_finished = True


if __name__ == "__main__":
    t = threading.Thread(target=print_loading_indicator)
    t.start()

    do_sth_time_consuming()
