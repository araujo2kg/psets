class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if (self._size + n) > self.capacity:
            raise ValueError("Exceeding jar capacity!")
        self._size = self._size + n

    def withdraw(self, n):
        if (self._size - n) < 0:
            raise ValueError("Not enough cookies!")
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid capacity(Negative integer)")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size=0):
        self._size = size


def main():
    my_jar = Jar(15)
    my_jar.deposit(5)
    my_jar.withdraw(2)
    print(my_jar)
    print(my_jar.size)


if __name__ == "__main__":
    main()
