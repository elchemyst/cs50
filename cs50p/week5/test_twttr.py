from twttr import shorten
import pytest


def test_str():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"

def test_caps():
    # Intentionally fails
    assert shorten("AB CD EF") == "B CD F"

def test_punctuation():
    assert shorten("ab,cd;ef.") == "b,cd;f."