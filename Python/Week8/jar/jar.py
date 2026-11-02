class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.n = 0

    def __str__(self):
        return self.n*'🍪'

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError
        else:
            self.n += n

    def withdraw(self, n):
        if n > self.n:
            raise ValueError
        else:
            self.n = self.n - n

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        self.size = self.n
        return self.size
