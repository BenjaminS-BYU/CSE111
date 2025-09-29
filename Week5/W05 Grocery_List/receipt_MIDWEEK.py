# Imports
import datetime
import csv
# Define some globals
SALES_TAX = 0.06
PRODUCTS_CSV = "products.csv"
REQUEST_CSV = "request.csv"
KEY_COLUMN_INDEX = 0
VALUE_COLUMN_INDEX = 1
products_dictionary = {}



def main():
    # Call the read_dictionary function, store the returned 
    # dictionary in the variable products_dict. Display the dictionary.
    products_dict = read_dictionary(PRODUCTS_CSV, KEY_COLUMN_INDEX)
    print(products_dict)

    # Open the request.csv file for reading.
    with open(REQUEST_CSV) as request_file:
        # Skip the first line of the request.csv 
        # file because the first line contains column headings.
        next(request_file)

        
        # Uses a loop to read and processes each row from the request.csv file.
        print("Requested items:") 
        reader = csv.reader(request_file)
        for row in reader:
        # Within the body of the loop, your program must do the following for each row:
            # Use the requested product number to find the corresponding item in the products_dict.
            prod_number = row[0]
            quantity = row[1]
            if prod_number in products_dict:
                print(f"{products_dict[prod_number][0]}: {quantity} @ ${products_dict[prod_number][1]}")

def read_dictionary(filename, key_column_index) -> dict:
    """open a CSV file for reading and use a csv.reader to 
    read each row and populate a compound dictionary with the 
    contents of the products.csv file."""
    with open(filename) as file:
        # Skip the first row
        next(file)
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(file)
        # Read the rows in the CSV file one row at a time.
        # The first item is the key, the value is a list of the 
        # Name and price of the product
        for row in reader:
            product_id = row[key_column_index].strip()
            name_price = row[1].strip(), row[2].strip()
            products_dictionary[product_id] = name_price
    return products_dictionary

# Display the order receipt.
    # Print a store name (you choose the name) at the top of the receipt.
    # Print the list of ordered items. Include the item name, quantity ordered and price per item.
    # Sum and print the number of ordered items.
    # Sum and print the subtotal due.
    # Compute and print the sales tax amount. Use 6% as the sales tax rate.
    # Compute and print the total amount due.
    # Print a thank you message.
    # Get the current date and time from your computer’s operating system and print the current date and time.
    # Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.

if __name__ == "__main__":
    main()