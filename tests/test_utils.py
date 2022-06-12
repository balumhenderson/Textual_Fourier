import pytest

def test_simple_addition():
    one = 1
    expected = 2
    actual = one + one
    assert actual == expected

def test_assersion_error():
    expected = 2
    actual = 3
    with pytest.raises(AssertionError):
        assert actual == expected

def test_raise_exception():
    def func():
        return 1 / 0
    with pytest.raises(ZeroDivisionError):
        func()
