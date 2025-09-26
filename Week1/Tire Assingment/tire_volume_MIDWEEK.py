import math
# Enter the width of the tire in mm (ex 205): 185
# Enter the aspect ratio of the tire (ex 60): 50
# Enter the diameter of the wheel in inches (ex 15): 14
# The approximate volume is 24.09 liters

# Enter the width of the tire in mm (ex 205): 205
# Enter the aspect ratio of the tire (ex 60): 60
# Enter the diameter of the wheel in inches (ex 15): 15
# The approximate volume is 39.92 liters

width_of_tire = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_inches = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = ((math.pi * (width_of_tire**2) * aspect_ratio)*(width_of_tire*aspect_ratio + 2540 * diameter_inches))/10000000000

print(f"The approximate volume is {volume:.2f} liters")

# v is the volume in liters everything should equal this
# π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# w is the width of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the diameter of the wheel in inches.