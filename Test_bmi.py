import bmi

print("Test bmi.py")


def test_underweight():
    result = bmi.calculate_bmi(weight=57, height=1.8)
    assert (result == -1)


def test_normalweight():
    result = bmi.calculate_bmi(weight=57, height=1.73)
    assert (result == 0)


def test_overweight():
    result = bmi.calculate_bmi(weight=57, height=1.50)
    assert (result == 1)
