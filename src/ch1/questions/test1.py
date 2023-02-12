from re import L


def test_1():
    assert [1, 2, 3] == [1, 2, 3]

def test_2():
    assert [1, 2, 3] == [1, 3, 2]

def test_3():
    assert 1 == 1

def test_4():
    assert 1 == 1.0

def test_5():
    assert 1 == "1"