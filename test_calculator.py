import pytest
from calculator import add, subtract, multiply, divide, clear

def test_add():
    assert add(2, 2) == 4

def test_subtract():
    assert subtract(5, 4) == 1

def test_multiply():
    assert multiply(6, 7) == 42

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_negative_numbers():
    assert add(-4, -6) == -10

def test_decimal_numbers():
    assert divide(7, 2) == 3.5

def test_large_numbers():
    assert add(999999999, 1) == 1000000000

def test_clear():
    assert clear() == 0
