import threading


def main():
    # fmt: off
    '''
    lock = threading.Lock()

    def print_odd() -> None:
        for i in range(1, 100, 2):
            with lock:
                print("odd ", i)

    def print_even() -> None:
        for i in range(2, 101, 2):
            with lock:
                print("even", i)

    t1 = threading.Thread(
        target=print_odd,
        args=(),
    )

    t2 = threading.Thread(
        target=print_even,
        args=(),
    )

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    '''
    # fmt: on

    odd_lock = threading.Lock()

    even_lock = threading.Lock()
    even_lock.acquire()

    def print_odd() -> None:
        for i in range(1, 100, 2):
            odd_lock.acquire()
            print("odd ", i)
            even_lock.release()

    def print_even() -> None:
        for i in range(2, 101, 2):
            even_lock.acquire()
            print("even", i)
            odd_lock.release()

    t1 = threading.Thread(
        target=print_odd,
        args=(),
    )
    t2 = threading.Thread(
        target=print_even,
        args=(),
    )

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def main_v2():
    lock = threading.Lock()

    ODD_TURN = 1
    EVEN_TURN = 0
    turn = ODD_TURN

    def print_odd() -> None:
        nonlocal turn

        for i in range(1, 100, 2):
            while turn != ODD_TURN:
                pass

            print("odd ", i)

            with lock:
                turn = EVEN_TURN

    def print_even() -> None:
        nonlocal turn

        for i in range(2, 101, 2):
            while turn != EVEN_TURN:
                pass

            print("even", i)

            with lock:
                turn = ODD_TURN

    t1 = threading.Thread(
        target=print_odd,
        args=(),
    )
    t2 = threading.Thread(
        target=print_even,
        args=(),
    )

    t1.start()
    t2.start()

    t1.join()
    t2.join()


class OddEvenConditionVariable(threading.Condition):
    """
    Recall from the Python docs:
        "
        A condition variable is always associated with some kind of lock;
        ...
        The lock is part of the condition object:
        you don't have to track it separately.
        "
    """

    ODD_TURN = True
    EVEN_TURN = False

    def __init__(self) -> None:
        super().__init__()
        self.turn = self.ODD_TURN

    def wait_turn(self, old_turn: bool) -> None:
        with self:
            while self.turn != old_turn:
                self.wait()  # Releases the lock, and then blocks until another thread awakens it by calling `notify()` or `notify_all()`

    def toggle_turn(self) -> None:
        with self:
            # self.turn ^= True
            self.turn = not self.turn
            self.notify()


class OddThread(threading.Thread):
    def __init__(self, o_e_cv: OddEvenConditionVariable) -> None:
        super().__init__()
        self.o_e_cv: OddEvenConditionVariable = o_e_cv

    def run(self) -> None:
        for i in range(1, 101, 2):
            self.o_e_cv.wait_turn(OddEvenConditionVariable.ODD_TURN)
            print(i)
            self.o_e_cv.toggle_turn()


class EvenThread(threading.Thread):
    def __init__(self, o_e_cv: OddEvenConditionVariable) -> None:
        super().__init__()
        self.o_e_cv: OddEvenConditionVariable = o_e_cv

    def run(self) -> None:
        for i in range(2, 101, 2):
            self.o_e_cv.wait_turn(OddEvenConditionVariable.EVEN_TURN)
            print(i)
            self.o_e_cv.toggle_turn()


def main_v3():
    odd_even_cond_var = OddEvenConditionVariable()
    t1 = OddThread(odd_even_cond_var)
    t2 = EvenThread(odd_even_cond_var)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def main_v4():
    ODD_TURN = True
    EVEN_TURN = False

    class AuxiliaryConditionVariable(threading.Condition):
        def __init__(self) -> None:
            super().__init__()
            self.turn = ODD_TURN

    aux_c_v = AuxiliaryConditionVariable()

    def print_odd():
        for i in range(1, 101, 2):
            with aux_c_v:
                while aux_c_v.turn != ODD_TURN:
                    aux_c_v.wait()

            print("[v4 >> odd ]", i)

            with aux_c_v:
                aux_c_v.turn = not aux_c_v.turn
                aux_c_v.notify()

    def print_even():
        for i in range(2, 101, 2):
            with aux_c_v:
                while aux_c_v.turn != EVEN_TURN:
                    aux_c_v.wait()

            print("[v4 >> even]", i)

            with aux_c_v:
                aux_c_v.turn = not aux_c_v.turn
                aux_c_v.notify()

    t1 = threading.Thread(target=print_odd)
    t2 = threading.Thread(target=print_even)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def main_v5():
    """
    Unlike `main_v4`,
    this solution has decoupled `turn` from the `threading.Condition` object,
    at the expense of having to use (closures,
    which here boils down to) 1 `nonlocal` variable.
    """

    ODD_TURN = True
    EVEN_TURN = False

    turn = ODD_TURN

    c_v = threading.Condition()

    def print_odd():
        nonlocal turn

        for i in range(1, 101, 2):
            with c_v:
                while turn != ODD_TURN:
                    c_v.wait()

            print("[v5 >> odd ]", i)

            with c_v:
                turn = not turn
                c_v.notify()

    def print_even():
        nonlocal turn

        for i in range(2, 101, 2):
            with c_v:
                while turn != EVEN_TURN:
                    c_v.wait()

            print("[v5 >> even]", i)

            with c_v:
                turn = not turn
                c_v.notify()

    t1 = threading.Thread(target=print_odd)
    t2 = threading.Thread(target=print_even)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def main_v6():
    """
    Unlike `main_v5`,
    this solution doesn't rely on (closures, i.e. on) any `nonlocal` variables,
    at the expense of having to convert the integer `turn` into the `turn_2_value` dict.

    Question: What is the difference between this function and `main_v2`?
    """

    ODD_TURN = True
    EVEN_TURN = False

    turn_2_value = {"turn": ODD_TURN}

    condition_variable = threading.Condition()

    def print_odd(t_2_v, c_v):

        for i in range(1, 101, 2):
            with c_v:
                while t_2_v["turn"] != ODD_TURN:
                    c_v.wait()

            print("[v6 >> odd ]", i)

            with c_v:
                t_2_v["turn"] = not t_2_v["turn"]
                c_v.notify()

    def print_even(t_2_v, c_v):

        for i in range(2, 101, 2):
            with c_v:
                while t_2_v["turn"] != EVEN_TURN:
                    c_v.wait()

            print("[v6 >> even]", i)

            with c_v:
                t_2_v["turn"] = not t_2_v["turn"]
                c_v.notify()

    t1 = threading.Thread(
        target=print_odd,
        args=(turn_2_value, condition_variable),
    )
    t2 = threading.Thread(
        target=print_even,
        args=(turn_2_value, condition_variable),
    )

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main_v6()
