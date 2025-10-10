import pytest
from Calories import format_input, remove_food, add_food, csv_to_list, get_quote 


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

def test_remove_food(tmp_path):
    """Test the remove_food function to ensure it correctly removes food items from the list."""
    # Create a temporary CSV file for testing
    test_file = tmp_path / "test_daily_food.csv"
    test_file.write_text("2025, 10, 10\n8945,Apple,95.0\n2859,Banana,105.0\n1234,Cherry,50.0\n")

    # Initial list of foods
    food_list = [
        ["2025", "10", "10"],
        ["8945", "Apple", "95.0"],
        ["2859", "Banana", "105.0"],
        ["1234", "Cherry", "50.0"]
    ]

    # Remove an existing food item
    remove_food("Banana", test_file)
    updated_list = []
    with open(test_file, 'r') as file:
        for line in file:
            updated_list.append(line.strip().split(','))

    assert ["2859", "Banana", "105.0"] not in updated_list
    assert len(updated_list) == 3  # One item should be removed

    # Attempt to remove a non-existing food item
    remove_food("Mango", test_file)
    updated_list_after_nonexistent = []
    with open(test_file, 'r') as file:
        for line in file:
            updated_list_after_nonexistent.append(line.strip().split(','))

    assert len(updated_list_after_nonexistent) == 3  # List should remain unchanged

def test_add_food(tmp_path):
    """Test the add_food function to ensure it correctly adds food items to the list."""
    # Create a temporary CSV file for testing
    test_file = tmp_path / "test_daily_food.csv"
    test_file.write_text("2025, 10, 10\n8945,Apple,95.0\n2859,Banana,105.0\n")

    # Initial list of foods
    food_list = [
        ["2025", "10", "10"],
        ["8945", "Apple", "95.0"],
        ["2859", "Banana", "105.0"]
    ]

    # Add a new food item food_file, food, total_cals, name_list
    add_food(test_file,1234,"Cherry", 50.0,"file")
    updated_list = []
    with open(test_file, 'r') as file:
        for line in file:
            updated_list.append(line.strip().split(','))

    assert ["1234", "Cherry", "50.0"] in updated_list
    assert len(updated_list) == 4  # One item should be added
    assert updated_list[-1] == ["1234", "Cherry", "50.0"]  # New item should be at the end


def test_csv_to_list(tmp_path):
    """Test the csv_to_list function to ensure it correctly reads a CSV file into a list of lists."""
    # Create a temporary CSV file for testing
    test_file = tmp_path / "test_daily_food.csv"
    test_file.write_text("2025, 10, 10\n8945,Apple,95.0\n2859,Banana,105.0\n1234,Cherry,50.0\n")

    expected_list = [
        ["8945", "Apple", "95.0"],
        ["2859", "Banana", "105.0"],
        ["1234", "Cherry", "50.0"]
    ]
    tmp_list = []
    result = csv_to_list(test_file, tmp_list)
    assert tmp_list == expected_list



# def test_get_quote():
#     """Test the get_quote function to ensure it returns a non-empty string."""
#     quotes = ["The only way to do great work is to love what you do. - Steve Jobs",
#               "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
#               "Don't watch the clock; do what it does. Keep going. - Sam Levenson",]
    
#     quote = get_quote(quotes)
#     assert isinstance(quote, str)
#     assert len(quote) > 0  # Ensure the quote is not an empty string

pytest.main(["-v", "--tb=line", "-rN", __file__])
