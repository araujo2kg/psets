from jar import Jar


def test_construct():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jarjar = Jar(5)
    assert jarjar.capacity == 5
    assert jarjar.size == 0


def test_str_():
    jar1 = Jar()
    jar1.deposit(3)
    assert str(jar1) == "🍪🍪🍪"
    jar2 = Jar()
    jar2.deposit(5)
    assert str(jar2) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jarbinks = Jar()
    jarbinks.deposit(10)
    assert jarbinks.size == 10


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5


def test_capacity():
    jar = Jar(5)
    assert jar.capacity == 5


def test_size():
    jar = Jar()
    jar.deposit(12)
    assert jar.size == 12
