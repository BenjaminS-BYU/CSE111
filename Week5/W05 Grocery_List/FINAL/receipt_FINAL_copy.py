# Imports
from datetime import datetime, timedelta
import csv
# Define some globals
SALES_TAX = 0.06
PRODUCTS_CSV = "C:/Users/baggi/OneDrive - BYU-Pathway Worldwide/Desktop/Coding/BYU/CSE111/Week5/W05 Grocery_List/products.csv"
REQUEST_CSV = "C:/Users/baggi/OneDrive - BYU-Pathway Worldwide/Desktop/Coding/BYU/CSE111/Week5/W05 Grocery_List/request.csv"
KEY_COLUMN_INDEX = 0
VALUE_COLUMN_INDEX = 1
products_dictionary = {}



def main():
    # Print a store name (you choose the name) at the top of the receipt.
    # Print the store name
    print("Some Frills Included")
    # Call the read_dictionary function, store the returned 
    # dictionary in the variable products_dict. Display the dictionary.
    try:
        products_dict = read_dictionary(PRODUCTS_CSV, KEY_COLUMN_INDEX)
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit()
    except PermissionError as e_p:
        print(e_p)
        exit()

    # Open the request.csv file for reading.
    with open(REQUEST_CSV) as request_file:
        # Skip the first line of the request.csv 
        # file because the first line contains column headings.
        next(request_file)

        
        # Uses a loop to read and processes each row from the request.csv file.
        print("Requested items:\n") 
        reader = csv.reader(request_file)
        subtotal = 0
        for row in reader:
        # Within the body of the loop, your program must do the following for each row:
            # Use the requested product number to find the corresponding item in the products_dict.
            try:
                prod_number = row[0]
                quantity = int(row[1])
                name = products_dict[prod_number][0]
                price = float(products_dict[prod_number][1])
                subtotal += price * quantity
                
                if prod_number in products_dict:
                    # Print the list of ordered items. Include the item name, quantity ordered and price per item.
                    print(f"{name}: {quantity} @ ${price}")
            except KeyError as e:
                print("Error: unknown product ID in the request.csv file")
                print(e)
    #Sum and print the number of ordered items.
    # Sum and print the subtotal due.
    # Compute and print the sales tax amount. Use 6% as the sales tax rate.
    # Compute and print the total amount due.
    tax = subtotal * SALES_TAX
    total = tax + subtotal
    date = datetime.now().strftime('%a %b %d %H:%M:%S %Y')  # Wed Nov 04 05:10:30 2020

    # Sales date: 30 days from now
    sale_date = datetime.now() + timedelta(days=30)
    days_left = (sale_date - datetime.now()).days
    
    # Prints a receipt format
    receipt = f"""
    ========================================
            Some Frills Included
    ========================================
    Date: {date}

    Subtotal:       ${subtotal:>8.2f}
    Sales Tax:      ${tax:>8.2f}
    ----------------------------------------
    TOTAL:          ${total:>8.2f}
    ========================================
        Next Sale: {sale_date.strftime("%Y-%m-%d")}
        Only {days_left} days left!
    ========================================
        Thank you for shopping!
    ========================================
    """
    print(receipt)
    

def read_dictionary(filename, key_column_index):
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

    

if __name__ == "__main__":
    main()