from datetime import datetime
subtotal:float = 0.0
SALES_TAX:float = 0.06
sale = 0.1
discount = 0
# Your program asks the user for the subtotal but does not ask the user for the day of the week. 
while subtotal <= 0.0:
    subtotal = float(input("What is the subtotal? "))
    
# Your program gets the day of the week from your computer’s operating system.
day_of_the_week = datetime.now()
current_day = day_of_the_week.date().weekday()
weekday_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

def sales_total():
    sales_tax_amount = subtotal * SALES_TAX
    total = subtotal + sales_tax_amount
    print(f"Sales tax amount is ${sales_tax_amount:.2f}")
    print(f"The total is ${total:.2f}")

# If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. 
# Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. 
# Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.
# You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s 
# slowest sales days. On Tuesday and Wednesday, if a customer’s 
# subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.

def day_of_the_week_sale(test_day:int,day:str,sale:float):
    if subtotal >= 50 and (test_day == 1 or test_day == 2):
        # Get the discount by taking subtotal and * 0.10 ex. 50 * 0.10 = $5
        discount = subtotal * sale
        # Calculate the new subtotal by - the discount number ex. $5
        discounted_sub = subtotal - discount
        # Calculate the sales tax by getting the new subtotal and * by 0.06 ex, 45 * 0.06 = $2.7
        sales_tax_amount = discounted_sub * SALES_TAX
        # Now add the sales tax to the subtotal and make it the total $45 + $2.7 = $47.7
        total = discounted_sub + sales_tax_amount
        print(f"Today is {day}, discount added: -${discount:.2f}")
        print(f"${discounted_sub:.2f}")
        print(f"Sales tax amount is ${sales_tax_amount:.2f}")
        print(f"The total is ${total:.2f}")
    elif subtotal < 50 and (test_day == 1 or test_day == 2):
        (f"Today is {day}")
        amount_to_discount = 50 - subtotal
        print(f"You are ${amount_to_discount} away from discount pricing")
        sales_total()
    else:
        print(f"Today is {day}")
        sales_total()


day_of_the_week_sale(current_day,weekday_dict[current_day],0.10)

# Your program correctly computes and prints the discount amount if applicable.
# Your program correctly computes and prints the sales tax amount and the total amount due.
