from datetime import datetime
import csv
import random
"""This program is aimed at helping people track their calorie intake from a list of foods and new foods they add. This program will let you add food, remove food, look at a quote for motivation 
and will calculate the total caloric intake for that day and add the users input into an empty txt file that empties if the 
date is different."""

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
2. Remove Food (working)
3. Your Food (working)
4. Change Quote (Working)
5. Exit (Working)
    """)
        users_choice = input("Your choice: ")

        if users_choice == "5":
            print("Have a great day!")
            print(get_quote(quotes_dict))
            exit()

        elif users_choice == "1":
            food = input("What food would you like to add? ")
            formatted_user = format_input(food)
            if formatted_user in food_dict:
                grams = float(input("What are the grams? "))
                calories = float(food_dict[formatted_user])
            else:
                confirm = input(f"Are you sure you want to add {formatted_user}? (y/n): ").lower()
                if confirm == "n":
                    continue
                elif confirm == "y":
                    calories = float(input("What are the calories per 100 grams? "))
                    grams = float(input("How many grams did you have? "))
                    add_food(FOOD_DICT,formatted_user,calories, "known foods")
                else:
                    print("Input not supported")
                    continue
            total_cals = (calories/100)*grams
            add_food(DAILY_FOOD,formatted_user,total_cals, "daily foods")

        elif users_choice == "2":
            show_food()
            rmv_food = input("Which food item would you like to remove? ")
            formatted_rvm = format_input(rmv_food)
            remove_food(formatted_rvm,DAILY_FOOD)
            show_food()

        elif users_choice == "3":
            show_food()

        elif users_choice == "4":
            quote= get_quote(quotes_dict)

        else:
            print("Input not valid, please try again")


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
    


def add_food(food_file, food, total_cals, name_list):
    """This function will allow the user to add a food and its calories to the 
list of a csv file"""
    with open(food_file, "a") as food_file:
        food_file.write(f"{food}, {total_cals}\n")
    print(f"{food} was add to the {name_list} list.")


# WORK ON THIS
def remove_food(food, food_file):
    """This function takes the food prama and take it out of 
the list txt file from the days list"""
    for line in list(daily_dict.keys()):
        if line == food:
            del daily_dict[line]
    try:
        with open(food_file, "r", newline="" ) as food_list:
            rows = list(csv.reader(food_list))

        rows = [row for row in rows if row[0] != food]

        with open(food_file, "w", newline='') as food_list:
            writer = csv.writer(food_list)
            writer.writerows(rows)

        print(f"{food} was removed.")
            
    except FileNotFoundError:
        print("File not found")

def show_food():
    """This shows the list txt that holds the food added"""
    total_cals = 0
    food_dict_maker(DAILY_FOOD,daily_dict)
    print("Your foods for the day:\n")
    for key, value in daily_dict.items():
        print(f"{key}: {value}kals")
        total_cals += float(value)
    print(f"Total calories for today is {total_cals}kals\n")
    enter = input("Hit enter to continue ")
    if enter == "":
        return



def get_quote(quotes):
    """goes into the quote txt and picks a random quote to show"""
    num = str(random.randint(1,len(quotes)))
    quote = quotes[num]
    return f"{quote.strip()}!"
        

def format_input(user_input):
    """This function takes the users input like '  apple  ' 
and standardizes it to to strip it and capitalizes it and 
returns the outcome 'Apple'"""
    return user_input.strip().capitalize()


# For testing purposes don't call main when testing
if __name__ == "__main__":
    main()