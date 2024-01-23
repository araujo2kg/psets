from seasons import Birth
from unittest import mock


def test_get_date_default():
    with mock.patch("builtins.input", return_value="2000-03-21"):
        assert Birth.get_date() == Birth(2000, 3, 21)
    with mock.patch("builtins.input", return_value="1999-01-10"):
        assert Birth.get_date() == Birth(1999, 1, 10)


def test_get_age_minutes():
    assert Birth.get_age_minutes(Birth(2000, 3, 21)) == 12520800


def test_sing():
    assert (
        Birth.sing(Birth(2000, 3, 21))
        == "Twelve million, five hundred twenty thousand, eight hundred minutes"
    )
