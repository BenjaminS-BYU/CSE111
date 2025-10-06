from datetime import datetime
import csv
import random
"""This program is aimed at helping people track their calorie intake from a list of foods and new foods they add. This program will let you add food, remove food, look at a quote for motivation 
and will calculate the total caloric intake for that day and add the users input into an empty txt file that empties if the 
date is diffrent."""

# Consts
FOOD_DICT = "common_foods_with_mealplan.csv"
DAILY_FOOD = "daily_food_calories.csv"
QUOTES_TXT = "motivational_weight_loss_quotes.txt"
KEY_INDEX = 0
VALUE_INDEX = 1

# Global dicts
food_dict = {}
quote_dict = {}
daily_dict = {}

def main():
    food_dict_maker(FOOD_DICT,food_dict)
    quotes_dict = motivation_dict_maker(QUOTES_TXT)
    todays_date(DAILY_FOOD)

    quote= get_quote(quotes_dict)
    

    while True:
        print("="*(len(quote)))
        print(quote)
        print("="*(len(quote)))
        print("""Welcome to the calorie tracking program. Please pick from the following:

Menu:
1. Add Food (Working)
2. Remove Food (Not working yet)
3. Your Food (working)
4. Change Quote (Working)
5. Exit (Working)
    """)
        users_choice = input("Your choice: ")

        if users_choice == "5":
            print("Have a great day!")
            exit()
        elif users_choice == "1":
            food = input("What food would you like to add? ")
            fomatted_user = format_input(food)
            print(add_food(fomatted_user,DAILY_FOOD))

        elif users_choice == "2":
            pass
        elif users_choice == "3":
            total_cals = 0
            food_dict_maker(DAILY_FOOD,daily_dict)
            print("Your foods for the day:\n")
            for key, value in daily_dict.items():
                print(f"{key}: {value}kals")
                total_cals += float(value)
            print(f"Total calories for today is {total_cals:.2f}")

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
            key = seperate_line[KEY_INDEX]
            quote = seperate_line[VALUE_INDEX]
            quote_dict[key] = quote
    return quote_dict

def food_dict_maker(csv_file, _dict):
    """Takes in the list given from the csv file and returns a dictionary"""
    with open(csv_file) as food_file_csv:
        next(food_file_csv)

        reader = csv.reader(food_file_csv)

        for line in reader:
            key = line[KEY_INDEX]
            value = line[VALUE_INDEX]

            _dict[key] = value

    return _dict

def todays_date(food_file):
    """This function overwrite the existing food file if the date has changed"""
    today = datetime.today()
    formatted_date = today.strftime("%Y, %d, %m")

    try:
        with open(food_file, "r") as daily_food_read:
            first_line = daily_food_read.readline().strip()
    except FileNotFoundError:
        first_line = ""

    if first_line != formatted_date:
        with open(food_file, "w") as daily_food:
            daily_food.write(f"{formatted_date}\n")
    


def add_food(food, food_file):
    """This function will allow the user to add a food to the 
list of a txt file"""
    if food in food_dict:
        grams = int(input("What are the grams? "))
        calories = float(food_dict[food])
    else:
        calories = int(input("What are the calories per 100 grams? "))
        grams = int(input("How many grams? "))
    total_cals = (calories/100)*grams
   
    with open(food_file, "a") as daily_food:
        daily_food.write(f"{food}, {total_cals}\n")
    return f"{food} was add to the daily list."


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