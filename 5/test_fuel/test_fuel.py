from fuel import convert, gauge
import pytest

def test_convert_default():
    assert convert("1/4") == 25
    assert convert("3/4") == 75

def test_gauge_default():
    assert gauge(25) == "25%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_error_handle():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1.5/2.5")

