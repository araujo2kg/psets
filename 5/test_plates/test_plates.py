from plates import is_valid

def test_default():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_start_two():
    assert is_valid("52CS") == False
    assert is_valid("CS52") == True
    assert is_valid("A123") == False

def test_minmax_char():
    assert is_valid("A") == False
    assert is_valid("SIXCHARAC") == False
    assert is_valid("TEST") == True

def test_number_pos():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_special_char():
    assert is_valid("AA,222") == False
    assert is_valid("AAA 22") == False
    assert is_valid("AAA.22") == False
