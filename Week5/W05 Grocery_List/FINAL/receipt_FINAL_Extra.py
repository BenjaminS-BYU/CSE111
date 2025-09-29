# Benjamin Strong Sept. 29th 2025 CSE111
# Things I added:
# 1. With help from ChatGPT I formatted the receipt nicely and got a way to count down to the sales date
# 2. Added a return date and count down to it as well
# 3. Added the buy one get one 50% off. I had it so that if you bought 4, you'd get 2 at a discount. 
# Every even number of item is discounted and added to a list to add up the total saved amount  

# Imports
from datetime import datetime, timedelta
import csv
# Define some globals
SALES_TAX = 0.06
PRODUCTS_CSV = "products.csv"
REQUEST_CSV = "request.csv"
KEY_COLUMN_INDEX = 0
VALUE_COLUMN_INDEX = 1
products_dictionary = {}
# Buy one Get one 50%
BOGO = "D083" # D083,1 cup yogurt,0.75
BOGO_dict = {}



def main():
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
        reader = csv.reader(request_file)
        subtotal = 0
        print("\n==================== RECEIPT ====================")
        print(f"{'Item':<15}{'Qty':>5}{'Price':>10}")
        print("-" * 40)
        for row in reader:
        # Within the body of the loop, your program must do the following for each row:
            # Use the requested product number to find the corresponding item in the products_dict.
            try:
                prod_number = row[0]
                quantity = int(row[1])
                name = products_dict[prod_number][0]
                price = float(products_dict[prod_number][1])
                
                if prod_number in products_dict:
                    # Print the list of ordered items. Include the item name, quantity ordered and price per item.
                    print(f"{name:<15}{quantity:>5}\t${price:>5.2f}")
                # If the product number matches the discount for BOGO, then add it to the list and print a statement letting 
                # The user know it was added. This will still show up if the user just wants 1 item, so you could say
                # Its a little insentive to buy another.
                if prod_number == BOGO:
                    print(f"   BOGO 50% off: \t\t${price/2:.2f}")
                    for i in range(quantity):
                        prod_number_change = prod_number
                        prod_number_change = i + 1
                        if prod_number_change in BOGO_dict:
                            prod_number_change = len(BOGO_dict) + 1
                        BOGO_dict[prod_number_change] = price
                    continue
                subtotal += price * quantity

            except KeyError as e:
                print("Error: unknown product ID in the request.csv file")
                print(e)
    #Sum and print the number of ordered items.
    # Sum and print the subtotal due.
    # Compute and print the sales tax amount. Use 6% as the sales tax rate.
    # Compute and print the total amount due.

    # Add a saved list to add up all the sales prices to then show how much was saved.
    saved_list = []
    # Iterate through the dict of items and every even number get the sales price.
    for key in BOGO_dict.keys():
        if key % 2 == 0:
            BOGO_dict[key] = BOGO_dict[key]/2
            saved_list.append(BOGO_dict[key])
    for value in BOGO_dict.values():
        subtotal += value
    total_saved = sum(saved_list)


    tax = subtotal * SALES_TAX
    total = tax + subtotal
    date = datetime.now().strftime('%a %b %d %H:%M:%S %Y')  # Wed Nov 04 05:10:30 2020

    # Sales date: 30 days from now
    sale_date = datetime.now() + timedelta(days=30)
    days_left = (sale_date - datetime.now()).days

    # Returns are due in 7 days from now, we don't like dilly dallying
    return_date = datetime.now() + timedelta(days=7)
    # Return days left plus 1 to account for the day bought
    return_days_left = (return_date - datetime.now() ).days + 1
    
    # Prints a receipt format
    receipt = f"""
    ========================================
            Some Frills Included
    ========================================
    Date: 
            {date}
    Subtotal:       ${subtotal:>8.2f}
    Sales Tax:      ${tax:>8.2f}
    Total Saved     ${total_saved:>8.2f}
    ----------------------------------------
    TOTAL:          ${total:>8.2f}
    ========================================
            Next Sale: {sale_date.strftime("%Y-%m-%d")}
            Only {days_left} days left!
    ========================================
            Thank you for shopping!
    You have {return_days_left} days to return any returnable items
        return items by: {return_date.strftime("%Y-%m-%d")} 9:00pm 
===================================================
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