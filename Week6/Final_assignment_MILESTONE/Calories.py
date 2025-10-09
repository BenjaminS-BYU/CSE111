# THINGS TO ADD:
# - Add testing
# - Add a way to make sure a foods code isn't repeated
# - Add more try/excepts for file handling and user input
# - Add more safeguards for user input (i.e. no negative grams or calories, or non-numeric input or empty input)

from datetime import datetime
import csv
import random
"""This program is aimed at helping people track their calorie intake from a list of foods and new foods they add. 
This program will let you add food, remove food, look at a quote for motivation 
and will calculate the total caloric intake for that day and add the users input into an empty txt file that empties if the 
date is different."""

# Consts
FOOD_DICT = "common_foods_with_mealplan.csv"
DAILY_FOOD = "daily_food_calories.csv"
QUOTES_TXT = "motivational_weight_loss_quotes.txt"
KEY_INDEX = 0
VALUE_INDEX = 1

# Global dicts
food_dict = {} # This dict will hold the known foods and their calories
quote_dict = {} # This dict will hold the quotes


def main():
    """Gets the main inputs from the user and prints the results
    Also holds the main loop"""

    food_dict_maker(FOOD_DICT,food_dict) # Fills the food dict with known foods
    quotes_dict = motivation_dict_maker(QUOTES_TXT) # Fills the quote dict with quotes
    # Check if the date has changed and if so, overwrite the daily food file
    todays_date(DAILY_FOOD)


    quote= get_quote(quotes_dict) # Gets a random quote to start the program
    

    # Loops through the users inputs until they exit the program 
    while True:
        print("="*(len(quote))) # Print a line the length of the quote
        print(quote) # Print the quote
        print("="*(len(quote)))
        # Welcome message and menu
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
            end_quote = get_quote(quotes_dict)
            print("="*(len(end_quote)))
            print(end_quote)
            print("="*(len(end_quote)))
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
                    with open(FOOD_DICT, "a", newline='') as _known_foods:
                        _known_foods.write(f"{food}, {calories:.1f}\n")
                else:
                    print("Input not supported")
                    continue
            # Calculate the total calories given from the grams
            total_cals = float((calories/100)*grams)
            add_food(DAILY_FOOD,formatted_user,float(total_cals), "daily foods")

        # If 2 start to remove a food item
        elif users_choice == "2":
            show_food()
            rmv_food = input("Which food item would you like to remove? ex. 'peach' ")
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
            enter = input("Enter to continue... ")
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
            separate_line = line.split(".")
            key = separate_line[KEY_INDEX]
            quote = separate_line[VALUE_INDEX]
            quote_dict[key] = quote
    return quote_dict

def food_dict_maker(csv_file, _dict):
    """Takes in the list given from the csv file and returns a dictionary"""
    with open(csv_file) as food_file_csv:
        next(food_file_csv)

        reader = csv.reader(food_file_csv)

        for line in reader:
            key = line[KEY_INDEX]
            value = float(line[VALUE_INDEX])

            _dict[key] = value

    return _dict

def todays_date(food_file):
    """This function overwrite the existing food file if the date has changed"""
    today = datetime.today()
    formatted_date = today.strftime("%Y, %d, %m") # Year, Day, Month

    # Read the first line of the file to see if the date is the same
    try:
        with open(food_file, "r") as daily_food_read:
            first_line = daily_food_read.readline().strip()
    except FileNotFoundError:
        first_line = ""

    # If the date is different, overwrite the file
    if first_line != formatted_date: 
        with open(food_file, "w") as daily_food:
            daily_food.write(f"{formatted_date}\n")




def add_food(food_file, food, total_cals, name_list):
    """This function will allow the user to add a food and its calories to the 
list of a csv file"""
    code = random.randint(999, 10000) # Random code to identify the food uniqueley
    with open(food_file, "a", newline='') as food_file:
        # Append the code, food and its calories to the file
        food_file.write(f"{code},{food},{total_cals:.1f}\n")
    print(f"{food} was add to the {name_list} list.")



def remove_food(food, food_file):
    """This function will remove a food from the csv file by making a temp list of the csv file contents,
    removing the food from the temp list and rewriting the csv file with the temp list"""
    temp_list = [] 
    with open(food_file) as food_file_csv: # Read the csv file into a temp list
        reader = csv.reader(food_file_csv)
        for line in reader:
            temp_list.append(line)
    for line in temp_list:
        if food in line:
            temp_list.remove(line)
            print(f"{food} was removed from the daily foods list.")
            break
    with open(food_file, "w", newline='') as food_file_csv: # Rewrite the csv file with the temp list without the removed food
        writer = csv.writer(food_file_csv)
        writer.writerows(temp_list) 


    



def show_food():
    """This shows the list txt that holds the food added. It also calculates the total calories for the day"""
    daily_list = [] # This list will hold the foods added for the day
    total_cals = 0 # This will hold the total calories for the day
    # Read the daily food file into a list
    _list = csv_to_list(DAILY_FOOD,daily_list)

    max_name_len = max(len(line[1]) for line in _list) # Find the longest food name for formatting purposes
    max_cal_len = max(len(line[2]) for line in _list) # Find the longest calorie count for formatting purposes

    print("Your foods for the day:\n")
    # Print the foods in a formatted way without the codes
    for code, first_index, snd_index in daily_list:
        print(f"{first_index:<{max_name_len}} : {snd_index:<{max_cal_len}} kals")
        total_cals += float(snd_index)
    print(f"\nTotal calories for today is {total_cals:.1f}kals\n")
    # Buffer area so the user isn't just blasted with info
    enter = input("Enter to continue... ")
    if enter == "":
        return
    else:
        return


def csv_to_list(csv_file, _list):
    """This function takes in a csv file and returns a list of its contents"""
    with open(csv_file) as food_file_csv:
        next(food_file_csv)

        reader = csv.reader(food_file_csv) # Read the csv file into a list

        # Append each line to the list
        for line in reader:
            _list.append(line)

    return _list



def get_quote(quotes):
    """goes into the quote txt and picks a random quote to show"""
    num = str(random.randint(1,len(quotes))) # Randomly pick a number between 1 and the number of quotes
    quote = quotes[num] 
    return f"{quote.strip()}!" 
        

def format_input(user_input):
    """Formats the user input to match the known food list formatting"""
    return user_input.strip().capitalize() 



# For testing purposes don't call main when testing
if __name__ == "__main__":
    main()