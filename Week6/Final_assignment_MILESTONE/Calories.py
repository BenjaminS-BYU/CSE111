import datetime
import csv
import math
import random
"""This program is aimed at helping people track their calorie intake from a list of foods and new foods they add. This program will let you add food, remove food, look at a quote for motivation 
and will calculate the total caloric intake for that day."""

FOOD_DICT = "common_foods_with_mealplan.csv"
DAILY_FOOD = "daily_food_calories.txt"
QUOTES_TXT = "motivational_weight_loss_quotes.txt"
FOOD_NAME_INDEX = 0
FOOD_CAL_PER_100_INDEX = 1
food_dict = {}
quote_dict = {}

def main():
    food_dict_csv = food_dict_maker(FOOD_DICT)
    quotes_dict = motivation_dict_maker(QUOTES_TXT)

    quote= get_quote(quotes_dict)
    

    while True:
        print("="*(len(quote)))
        print(quote)
        print("="*(len(quote)))
        print("""Welcome to the calorie tracking program. Please pick from the following:

Menu:
1. Add Food
2. Remove Food
3. Your Food
4. Change Quote
5. Exit
    """)
        users_choice = input("Your choice: ")
        if users_choice == "5":
            print("Have a great day!")
            exit()
        elif users_choice == "1":
            food = input("What food would you like to add? ")
            fomatted_user = format_input(food)
            add_food(fomatted_user,food_dict_csv)
        elif users_choice == "2":
            pass
        elif users_choice == "3":
            pass
        elif users_choice == "4":
            quote= get_quote(quotes_dict)
            continue
        else:
            print("Input not valid, please try again")
            continue

def motivation_dict_maker(txt_file):
    """This function takes a txt file such as the quotes and turns it into a dict with the numbers as keys and 
    quotes as values"""
    with open(txt_file, encoding="utf-8") as file:
        next(file)

        for line in file:
            seperate_line = line.split(".")
            key = seperate_line[0]
            quote = seperate_line[1]
            quote_dict[key] = quote
    return quote_dict

def food_dict_maker(csv_file):
    """Takes in the list given from the csv file and returns a dictionary"""
    with open(csv_file) as food_file_csv:
        next(food_file_csv)

        reader = csv.reader(food_file_csv)

        for line in reader:
            key = line[FOOD_NAME_INDEX]
            value = line[FOOD_CAL_PER_100_INDEX]

            food_dict[key] = value

    return food_dict

def add_food(food, food_file):
    """This function will allow the user to add a food to the 
list on a txt file"""
    pass

def remove_food(food, food_file):
    """This function takes the food prama and take it out of 
the list txt file from the days list"""
    pass

def show_food(food_file):
    """This shows the list txt that holds the food added"""
    pass

def get_quote(quotes):
    """goes into the quote txt and picks a random quote to show"""
    num = str(random.randint(1,102))
    return f"{quotes[num]}!"
        

def format_input(user_input):
    """This function takes the users input like '  apple  ' 
and standardizes it to to strip it and upper case it and 
returns the outcome 'Apple'"""
    return user_input.strip().capitalize()


# For testing purposes don't call main when testing
if __name__ == "__main__":
    main()