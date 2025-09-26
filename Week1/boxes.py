import math

# A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
# Write a Python program named boxes.py that asks the user for two integers:

# the number of manufactured items
# the number of items that the user will pack per box
# Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. 
# Note that the last box may be packed with fewer items than the other boxes.

num_of_items = int(input("Enter the number of items: "))
num_per_box = int(input("Enter the number of items per box: "))

def item_calculation(box:int, item:int) -> int:
    round_number = math.ceil(box/item)
    return round_number

items_amount = item_calculation(num_of_items, num_per_box)

print(f"For {num_of_items} items, packing {num_per_box} items in each box, you will need {items_amount} boxes.")

# > python boxes.py
# Enter the number of items: 8
# Enter the number of items per box: 5
# For 8 items, packing 5 items in each box, you will need 2 boxes.
# > python boxes.py
# Enter the number of items: 25
# Enter the number of items per box: 4
# For 25 items, packing 4 items in each box, you will need 7 boxes

