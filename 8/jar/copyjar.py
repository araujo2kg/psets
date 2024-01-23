class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if (self.cookies + n) > self.capacity:
            raise ValueError("Exceeding jar capacity!")
        self.cookies = self.cookies + n

    def withdraw(self, n):
        if (self.cookies - n) < 0:
            raise ValueError("Not enough cookies!")
        self.cookies = self.cookies - n

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
        return self.size

    @size.setter
    def size(self, size):



def main():
    my_jar = Jar()
    my_jar.deposit(5)
    my_jar.withdraw(3)
    Jar.size()


if __name__ == "__main__":
    main()
