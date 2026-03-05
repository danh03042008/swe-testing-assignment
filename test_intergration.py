from calculator import add, subtract, multiply, divide, clear

def test_full_calculation_sequence():
    result = add(5, 3)
    result = subtract(result, 2)
    assert result == 6

def test_clear_resets_to_zero():
    result = add(10, 5)
    result = clear()
    assert result == 0
