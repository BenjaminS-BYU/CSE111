x = "moon"
y = "sun"
z = "stars"
# sep= is a way to divide up text in print statments
print(x,y,z, sep="|", flush=True)


# Modules:
# A Python module is a collection of related functions.
# Such as the math module and the random module 
# math.sqrt(x)
# From this short description, we know the following:
# 1. The name of the containing module is math.
# 2. The name of the function is sqrt.
# 3. The function accepts one parameter named x.
# 4. The function computes and returns the square root of the number that is in x.
# Example of this: 
# import math
# r = math.sqrt(71)
# print(r)

# Methods:
# Like a function, example: 

# Example 6
# Get a string of text from the user.
text1 = input("Enter a motivational quote: ")
# Call the built-in len function to get
# the number of characters in the text.
length = len(text1)
# Call the string upper method to convert
# the quote to upper case characters.
text2 = text1.upper()
# Call the built-in print function to print
# the length of the text and the text in all
# upper case for the user to see.
print(length, text2)


# len() is a function, .upper()**Gotta have these empty parentheses** is a method
