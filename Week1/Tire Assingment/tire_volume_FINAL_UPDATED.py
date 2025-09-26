# Benjamin Strong CSE111
# The changes I made: So I started with a while loop to keep the user entering tire sizes. Then I added a way to append them to a
# List then sort them by their last item which is the price so it will be highest to lowest
# Also changed the formatting more to my liking. the while loop is a bit duct-tapey but it works
# As long as the user types the right thing. ChatGPT helped 
# Me with this line specifically: tires.sort(key=lambda x: x[-1], reverse=True), so I had to make 
# Sure I understood it. It basically makes the sort method start from the back and reverse the order
# From ascending to descending. This took more time than I thought it would haha oof. 
# Output and formatting should look like this:
# For tire 1
### 2025-09-04, 205, 60, 15, 39.92 (Assignment output requirement)
# 205, 60, 15, 39.92, $205 (Extra credit output)
# Size: 205/60R15
# The approximate volume is 39.92 liters
# For tire 2
### 2025-09-04, 185, 50, 14, 24.09
# 185, 50, 14, 24.09, $156
# Size: 185/50R14
# The approximate volume is 24.09 liters



import math
from datetime import datetime

current_day = datetime.now()
tires: list[float]= []

# Opens a new txt file as a append text file so we can add stuff to it

# Ask for the width, aspect, and diameters
while True:
    width_of_tire = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter_inches = int(input("Enter the diameter of the wheel in inches (ex 15): "))
    price = int(input("Enter the price: "))
    # Calculate the total volume
    volume:float = ((math.pi * (width_of_tire**2) * aspect_ratio)*(width_of_tire*aspect_ratio + 2540 * diameter_inches))/10000000000
    volume = round(volume, 2)

    tires.append([width_of_tire,aspect_ratio,diameter_inches, volume, price]) # type: ignore
    
    user = input("Would you like to do another? (y/n): ").lower().strip()
    if user != "y":
        break
            

tires.sort(key=lambda x: x[-1], reverse=True) # type: ignore


with open ("volumes.txt", "at") as volumes_file:
    tire_num = 0

    for tire_list in tires: # type: ignore
        tire_num += 1
        print(tire_list) # type: ignore
        width = tire_list[0] # type: ignore
        aspect = tire_list[1] # type: ignore
        diameter = tire_list[2] # type: ignore
        volume_l = tire_list[3] # type: ignore
        price_l = tire_list[4] # type: ignore
        print(f"For tire {tire_num}", file=volumes_file)
        print(f"{current_day:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume_l}", file=volumes_file)
        print(f"{width}, {aspect}, {diameter}, {volume_l}, ${price_l}", file=volumes_file)
        print(f"Size: {width}/{aspect}R{diameter}", file=volumes_file)
        print(f"The approximate volume is {volume_l} liters", file=volumes_file) 

    
    