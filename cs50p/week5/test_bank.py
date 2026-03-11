from bank import value
import pytest


def test_value():
    assert value("hello") == 0
    assert value("Hello!") == 0


def test_20():
    assert value("h") == 20
    assert value("HI!") == 20


def test_100():
    assert value("What's up?") == 100
    assert value("Good Day!") == 100


def index_error():
    with pytest.raises(IndexError):
        value("")