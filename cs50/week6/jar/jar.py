#!/usr/bin/env python3
def main():
    jar = Jar()
    print(str(jar.capacity))


class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self.capacity = capacity
            self.jar = 0
        else:
            raise ValueError("Capacity must be non-negative")


    def __str__(self):
        for cookie in range(self.jar):
            print('🍪', end='')
            print()

    def deposit(self, n):
        if self.jar + n <= self.capacity:
            self.jar += 1
        else:
            raise ValueError("Exceeding jar's capacity")

    def withdraw(self, n):
        if n <= self.jar:
            self.jar -= n
        else:
            raise ValueError("Not that many cookies available")

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.jar


main()
