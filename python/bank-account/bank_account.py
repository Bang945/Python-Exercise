import threading


class BankAccount(object):

    # @with_lock failed
    # def wrapped(self, *args):
    #     with getattr(self, lock):
    #           return func((self, *args))
    #           TypeError: withdraw() missing 1 required positional argument: 'amount'
    def with_lock(lock):
        def wrapper(func):
            def wrapped(self, *args):
                with getattr(self, lock):
                    return func((self, *args))
            return wrapped
        return wrapper


    def is_open(func):
        def wrapped(self, *args):
            if self._valid is 0:
                raise ValueError("Account is closed.")
            return func(self, *args)
        return wrapped


    def __init__(self):
        self._balance = 0
        self._valid = 0
        self._lock = threading.Lock()


    @is_open
    def get_balance(self):
        return self._balance


    def open(self):
        self._valid = 1

    @is_open
    def deposit(self, amount):
        if (amount < 0):
            raise ValueError("Deposit shouldn't be negative.")

        with self._lock:
            self._balance += amount

    @is_open
    #@with_lock('_lock')
    def withdraw(self, amount):
        with self._lock:
            if (amount > self._balance 
                    or amount < 0):
                raise ValueError("Withdraw should be larger than balance.")
            self._balance -= amount


    def close(self):
        self._valid = 0