class Jar:
    def __init__(self, capacity=12):
        if not capacity >=0:
            raise ValueError('Invalid')
        self.capacity = capacity

    def __str__(self):
        return self.n*'🍪'

    def deposit(self, n):

        if n > Jar().__init__():
            raise ValueError
        else:
            self.n = n

    def withdraw(self, n):
        if n > self.n:
            raise ValueError
        else:
            self.n = self.n - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n
