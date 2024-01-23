from bank import value

def test_default():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("  Hello") == 0
    assert value("Hello  ") == 0
    assert value("!Hello") == 100
    assert value("Oh Hello") == 100

def test_h():
    assert value("How its going?") == 20
    assert value("How you doing?") == 20
    assert value("  How you doing?") == 20

def test_else():
    assert value("Whats up") == 100
    assert value("What's happening?") == 100
    assert value("Salamat pagi") == 100
