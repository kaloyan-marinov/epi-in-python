import threading


class Account:
    _global_id = 0

    def __init__(self, balance):
        self._balance = balance
        self._id = Account._global_id
        Account._global_id += 1
        self._lock = threading.RLock()

    def get_balance(self):
        return self._balance

    @staticmethod
    def transfer(acc_from, acc_to, amount):
        th = threading.Thread(
            target=acc_from._move,
            args=(acc_to, amount),
        )
        th.start()

    def _move(self, acc_to, amount):
        # fmt: off
        '''
        if self._id < acc_to._id:
            lock_1, lock_2 = self._lock, acc_to._lock
        else:
            lock_1, lock_2 = acc_to._lock, self._lock

        with lock_1, lock_2:
        '''
        # fmt: on
        with self._lock:
            print(f"{self._id} acquired lock")
            a = 0
            for _ in range(10 ** 9):
                # if a % (10 ** 8) == 0:
                #     print(a)
                a += 1

            if amount > self._balance:
                return False

            acc_to._balance += amount
            self._balance -= amount

            print("returning True")
            return True


if __name__ == "__main__":

    a_1 = Account(1000)
    a_2 = Account(1000)

    Account.transfer(a_1, a_2, 100)
    Account.transfer(a_2, a_1, 300)
