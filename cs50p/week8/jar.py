class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if self.cookies + n <= self.capacity:
            self.cookies += n
        else:
            raise ValueError("Jar capacity exceeded.")

    def withdraw(self, n):
        if self.cookies - n >= 0:
            self.cookies -= n
        else:
            raise ValueError("Not enough cookies.")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity or capacity < 0:
            raise ValueError("Capacity should be positive.")
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies