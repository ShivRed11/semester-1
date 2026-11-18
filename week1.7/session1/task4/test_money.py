# Reference solution (rewritten after original work was lost)
# Week 1.7, Session 1: Task 4 - unit tests for methods in Money

import pytest

from money import Money

def test_invalid_type_pound():
    with pytest.raises(TypeError) as excinfo:
        Money(1.2, 99)
    assert str(excinfo.value) == "pounds must be an integer"


def test_invalid_value_pound():
    with pytest.raises(ValueError) as excinfo:
        Money(-1, 0)
    assert str(excinfo.value) == "pounds must be >= 0"


def test_add_invalid_type():
    m1 = Money(5, 0)
    with pytest.raises(TypeError) as excinfo:
        m1 + 42
    assert str(excinfo.value) == "other object must be a Money"


def test_invalid_type_pence():
    # complete the test implementation for 
    # invalid type for pence
    # pytest.raises() passes only if the code inside the "with" raises TypeError
    with pytest.raises(TypeError) as excinfo:
        Money(1, 0.5)
    assert str(excinfo.value) == "pence must be an integer"
    

def test_invalid_value_pence():
    # complete the test implementation for 
    # invalid value for pence
    # test both sides of the valid range 0-99
    with pytest.raises(ValueError) as excinfo:
        Money(1, -1)
    assert str(excinfo.value) == "pence must be in range 0-99"

    with pytest.raises(ValueError) as excinfo:
        Money(1, 100)
    assert str(excinfo.value) == "pence must be in range 0-99"


def test_valid_constructor():
    # boundary values 0 and 99 for pence should be accepted
    m = Money(3, 0)
    assert m.pounds == 3
    assert m.pence == 0
    assert str(Money(0, 99)) == "£0.99"
    

def test_valid_add():
    # complete the test implementation for
    # valid add between money objects
    # Hint: you can compare using the __str()__ (
    # e.g., str(m1 + m2) == "£2.04"
    m1 = Money(1, 50)
    m2 = Money(0, 54)
    assert str(m1 + m2) == "£2.04"     # pence carry over into an extra pound

    # no carry needed
    assert str(Money(2, 10) + Money(3, 20)) == "£5.30"

    # exactly 100 pence -> one extra pound, 00 pence
    assert str(Money(0, 50) + Money(0, 50)) == "£1.00"
