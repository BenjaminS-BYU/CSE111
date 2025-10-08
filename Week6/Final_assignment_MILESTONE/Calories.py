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
    """Gets the main inputs from the user and prints the results
    Also holds the main loop"""
    food_dict_maker(FOOD_DICT,food_dict)
    quotes_dict = motivation_dict_maker(QUOTES_TXT)
    todays_date(DAILY_FOOD)

    quote= get_quote(quotes_dict)
    print("="*(len(quote)))
    print(quote)
    print("="*(len(quote)))

    # Loops through the users inputs until they exit the program 
    while True:
        print("""Welcome to the calorie tracking program. Please pick from the following:

Menu:
1. Add Food 
2. Remove Food 
3. Your Food 
4. Change Quote 
5. Exit 
    """)
        # Ask user for their choice
        users_choice = input("Your choice: ")

        # If 5, provide an exit quote and exit out completely
        if users_choice == "5":
            print("Have a great day!")
            print("="*(len(get_quote(quotes_dict))))
            print(get_quote(quotes_dict))
            print("="*(len(get_quote(quotes_dict))))
            exit()

        # Add food if 1
        elif users_choice == "1":
            food = input("What food would you like to add? ")
            formatted_user = format_input(food)

            # Check if in known list already
            if formatted_user in food_dict:
                grams = float(input("What are the grams? "))
                calories = float(food_dict[formatted_user])

            # If food is not, confirm they want to add it 
            else:
                confirm = input(f"Are you sure you want to add {formatted_user}? (y/n): ").lower()
                if confirm == "n":
                    continue
                # If yes then continue to add the grams and calories
                elif confirm == "y":
                    calories = float(input("What are the calories per 100 grams? "))
                    grams = float(input("How many grams did you have? "))
                    add_food(FOOD_DICT,formatted_user,calories, "known foods")
                else:
                    print("Input not supported")
                    continue
            # Calculate the total calories given from the grams
            total_cals = (calories/100)*grams
            add_food(DAILY_FOOD,formatted_user,total_cals, "daily foods")

        # If 2 start to remove a food item
        elif users_choice == "2":
            show_food()
            rmv_food = input("Which food item would you like to remove? ")
            formatted_rvm = format_input(rmv_food)
            remove_food(formatted_rvm,DAILY_FOOD)
            show_food()

        # If 3 just show the list of foods
        elif users_choice == "3":
            show_food()

        # If 4 change the quote 
        elif users_choice == "4":
            quote= get_quote(quotes_dict)

        # If they typed anything else, just restart
        else:
            print("Input not valid, please try again")
            # Buffer area so the user isn't just blasted with info
            enter = input("Enter to continue ")
            if enter == "":
                continue
            else:
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
    


def add_food(food_file, food, total_cals, name_list):
    """This function will allow the user to add a food and its calories to the 
list of a csv file"""
    with open(food_file, "a") as food_file:
        food_file.write(f"{food}, {total_cals:.1f}\n")
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
    max_key = max(len(key) for key in daily_dict)
    max_value = max(len(str(value)) for value in daily_dict.values())
    print("Your foods for the day:\n")
    for key, value in daily_dict.items():
        if key == key:
            key += "1"
### ADD HERE A WAY TO MAKE SURE ALL CASE OF THE SAME KEY BECOMES UNIQUE, LIKE IF THERE IS THREE PEACHES ON THE LIST

        print(f"{key:<{max_key}} : {value:>{max_value}} kals")
        total_cals += float(value)
    print(f"\nTotal calories for today is {total_cals}kals\n")
    # Buffer area so the user isn't just blasted with info
    enter = input("Enter to continue ")
    if enter == "":
        return
    else:
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