def main():
    start_reading = int(input("Enter the first odometer reading (miles): "))
    end_reading = int(input("Enter the second odometer reading (miles): "))
    fuel_amount = float(input("Enter the amount of fuel used (gallons): "))

    def calculate_mpg(start:int,end:int,gallon:float):
        mpg:float = (end-start)/gallon
        return mpg
    def mpg_to_l_per_100k():
        mpg = calculate_mpg(start_reading,end_reading,fuel_amount)
        liters = 235.215/mpg

        print(f"{mpg:.1f} miles per gallon")
        print(f"{liters:.2f} liters per 100 kilometers")
        return liters
    mpg_to_l_per_100k()

main()



# Write a Python program that asks the user for three numbers:

# A starting odometer value in miles
# An ending odometer value in miles
# An amount of fuel in gallons
# Your program must calculate and print fuel efficiency in both miles per gallon and liters per 100 kilometers. 
# Your program must have three functions named as follows:

# main
# miles_per_gallon
# lp100k_from_mpg
# All user input and printing must be in the main function. In other words, the miles_per_gallon and lp100k_from_mpg 
# functions must not call the the input or print functions.



# output = Enter the first odometer reading (miles): 30462
# Enter the second odometer reading (miles): 30810
# Enter the amount of fuel used (gallons): 11.2
# 31.1 miles per gallon
# 7.57 liters per 100 kilometers