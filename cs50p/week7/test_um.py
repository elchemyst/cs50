from um import count


def test_convert():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_false_count():
    li = [
        "cumquat",
        "jumpily",
        "gazumps",
        "flummox",
        "maximum",
        "jumbuck",
        "jejunum",
        "mazumas yum yum",
        "jumpoff"
    ]

    for s in li:
        assert count(s) == 0

def test_edge_cases():
    assert count("UM!") == 1
    assert count(" UMM ") == 0
    assert count("umumum") == 0