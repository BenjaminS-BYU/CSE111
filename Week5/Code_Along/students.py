import csv 
 
#initialize a dictonary 
student_dict = {}

def main():
    file = "students.csv"
    read_csv_file(file)
    print(student_dict)
    user_input = input("What ID do you want to look up? ")
    print(id_lookup(user_input, student_dict))
        


# Open the students.csv file for reading, skip the first line of text in the file because it contains only headings, 
# and read the other lines of the file into a dictionary. The program must store each student ID Number as a key and each 
# ID Number name pair or each name as a value in the dictionary.
def read_csv_file(filename):
    """Gets the file from the param and opens it and spits the list into a dictonary that was initalized globally"""
    with open(filename) as csv_file:
        # Skip the first row
        next(csv_file)
        # returns a dictonary
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
    """Look through the dictonary and find the value that is associated with the key given. Return the value. If key is not in dict, exit the program."""
    # Get an ID Number from the user, use the ID Number to find the corresponding student name in the dictionary, and print the name.

    if user_id in dic_name:
        name = dic_name[user_id]
        return name
    else:
        # If a user enters an ID Number that doesn’t exist in the dictionary, your program must print the message, 
        # "No such student" (without the quotes).
        print(f"No such student. The id {user_id} isn't in the database, try running the code again and put in a correct id.")
        exit()

if __name__ == "__main__":
    main()