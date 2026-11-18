# Reference solution (rewritten after original work was lost)
# Week 1.7, Session 1: Task 2 - unit test for comfort_level() 

# Fill in the blank spaces in the calls to comfort_level() below, using
# the values you've chosen for testing the function

# Then write a test_ok() function that tests the other equivalence class

from weather import comfort_level

# Each test checks a typical value AND the value right at the boundary


def test_cold():
    assert comfort_level(0.0) == "COLD"
    assert comfort_level(15.0) == "COLD"    # boundary: <= 15.0 is COLD

def test_hot():
    assert comfort_level(30.0) == "HOT"
    assert comfort_level(25.1) == "HOT"     # just above the 25.0 boundary

def test_ok():
    assert comfort_level(15.1) == "OK"      # just above the COLD boundary
    assert comfort_level(20.0) == "OK"
    assert comfort_level(25.0) == "OK"      # boundary: 25.0 is not > 25.0
