class Jar:
    def __init__(self, capacity=12):
        if not capacity >=0:
            raise ValueError('Invalid')
        self.capacity = capacity

    def __str__(self , n):
        return n*''


    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
