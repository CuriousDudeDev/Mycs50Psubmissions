class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._n = 0

    def __str__(self):
        return self._n*'🍪'

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError
        else:
            self._n += n

    def withdraw(self, n):
        if n > self._n:
            raise ValueError
        else:
            self._n = self._n - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n




