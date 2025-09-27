import csv  # Import the csv module for reading CSV files
import re   # Import the re module for regular expressions

"""
students.py
This module provides functionality to read student data from a CSV file, store it in a dictionary,
and allow lookup of student names by their ID numbers. It includes input sanitization to ensure
only valid numeric IDs are processed.
Functions:
    main():
        Entry point of the program. Reads student data from 'students.csv', prompts the user for an ID,
        sanitizes the input, and prints the corresponding student name or an error message.
    read_csv_file(filename):
        Reads a CSV file containing student IDs and names, skipping the header row, and populates
        the global student_dict with ID-name pairs.
    id_lookup(user_id, dic_name):
        Looks up a student name by ID in the provided dictionary. Returns the name if found,
        otherwise prints an error message and exits the program.
    remove_extras(u_input):
        Sanitizes user input by removing all non-digit characters using regular expressions,
        returning only the numeric portion of the input.
Global Variables:
    student_dict (dict): Stores student ID as keys and names as values.
"""

# Global
student_dict = {}

# Starts here
def main():
    """
    Main function to read student data from a CSV file, display the student dictionary,
    prompt the user for a student ID, clean the input, and look up the student information.
    Steps:
    1. Reads student data from 'students.csv' using read_csv_file(file).
    2. Prints the student dictionary (student_dict).
    3. Prompts the user to enter a student ID.
    4. Cleans the user input using remove_extras(user_input).
    5. Looks up and prints the student information using id_lookup(clean_number, student_dict).
    """
    while True:
        file = "students.csv"
        read_csv_file(file)
        print(student_dict)
        user_input = input("What ID do you want to look up? ")
        clean_number = remove_extras(user_input)
        print(id_lookup(clean_number, student_dict))
        again = input("Would you like to search another ID? (y/n): ")
        if again == "n":
            print("Goodbye")
            break
        else:
            continue
        


# Open the students.csv file for reading, skip the first line of text in the file because it contains only headings, 
# and read the other lines of the file into a dictionary. The program must store each student ID Number as a key and each 
# ID Number name pair or each name as a value in the dictionary.
def read_csv_file(filename):
    """Gets the file from the param and opens it and spits the list into a dictionary that was initialized globally"""
    with open(filename) as csv_file:
        # Skip the first row
        next(csv_file)
        # returns a dict
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:
            id = row[0].strip()
            name = row[1].strip()
            student_dict[id] = name
    return student_dict

def id_lookup(user_id, dic_name):
    """Look through the dict and find the value that is associated with the key given. 
    Return the value. If key is not in dict, exit the program."""
    # Get an ID Number from the user, use the ID Number to find the corresponding student name in the dictionary, and print the name.

    if user_id in dic_name:
        name = dic_name[user_id]
        return name
    else:
        # If a user enters an ID Number that doesn’t exist in the dictionary, your program must print the message, 
        # "No such student" (without the quotes).
        print(f"No such student. The id {user_id} isn't in the database, try running the code again and put in a correct id.")
        exit()

def remove_extras(u_input):
    """Takes the user input and runs through the re import to remove any character that isn't an int. 
    Returns the new input of just digits"""
    # Use regular expressions to remove any non-digit characters from the user input.
    clean_line = re.sub(r'\D', "", u_input)
    return clean_line

if __name__ == "__main__":
    main()