from numb3rs import validate

def test_validate_default():
    assert validate("0.0.0.0") == True
    assert validate("1.1.0.0") == True
    assert validate("0.0.0") == False

def test_validate_range():
    assert validate("300.0.0.0") == False
    assert validate("0.0.-1.0") == False
    assert validate("0.255.0.0") == True
    assert validate("0.0.256.0") == False

def test_validate_oct():
    assert validate("1.2.3.1000") == False

def test_validate_input():
    assert validate("cat") == False
    assert validate("         0.0.0.0") == False
