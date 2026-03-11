from plates import is_valid


def test_valids():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True


def test_invalid_nums():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS 50") == False


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI314!") == False


def test_str():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False