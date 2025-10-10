import pytest
from Calories import format_input

def test_format_input():
    """"Test the format_input function to ensure it correctly formats user input. 
    it should strip leading/trailing whitespace and convert to capitalized form."""
    assert format_input("  apple  ") == "Apple"
    assert format_input("BANANA") == "Banana"
    assert format_input("  cHeRrY ") == "Cherry"
    assert format_input("mango") == "Mango"
    assert format_input("  PeAr  ") == "Pear"
    assert format_input("") == ""
    assert format_input("   ") == ""
    assert format_input("123fruit") == "123fruit"
    assert format_input("fruit@home") == "Fruit@home"
    assert format_input("  mixed CASE Input  ") == "Mixed case input"

pytest.main(["-v", "--tb=line", "-rN", __file__])
