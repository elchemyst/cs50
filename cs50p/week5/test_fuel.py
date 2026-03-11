from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    with pytest.raises(ValueError):
        convert("cats & dogs")
    with pytest.raises(ValueError):
        convert("-3/4")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"