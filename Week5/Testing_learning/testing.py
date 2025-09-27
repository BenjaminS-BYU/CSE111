import math

try:
    cans = int(input("How many cans do you need to ship? "))
    cans_per_box = int(input("How many cans can fit into a box? "))
    boxes: int = math.ceil(cans/cans_per_box)
except ZeroDivisionError:
    print("You cannot enter a 0 for numbers of cans per box")
except ValueError:
    print("You must enter a whole number")
except Exception as e:
    print(f"Something went wrong. {e}")
else:
    print(f"You will need {boxes} boxes to ship all your cans.")
finally:
    print("ur done")


### CORRECT SYNTAX FOR TRY/EXCEPT
# Example 1
#try:
# Write normal code here. This block must include
# code that falls into two groups:
# 1. Code that may cause an exception to be raised
# 2. Code that depends on the results of the code
# in the first group
#except ZeroDivisionError as zero_div_err:
# Code that the computer executes if the code in the try
# block caused a function to raise a ZeroDivisionError.
#except ValueError as val_err:
# Code that the computer executes if the code in the
# try block caused a function to raise a ValueError.
#except (TypeError, KeyError, IndexError) as error:
# Code that the computer executes if the code in the
# try block caused a function to raise a TypeError,
# KeyError, or IndexError.
#except Exception as excep:
# Code that the computer executes if the code in the try
# block caused a function to raise any exception that
# was not handled by one of the previous except blocks.
#except:
# Code that the computer executes if the code in the
# try block caused a function to raise anything that
# was not handled by one of the previous except blocks.
#else:
# Code that the computer executes after the code
# in the try block if the code in the try block
# did not cause any function to raise an exception.
#finally:
# Code that the computer executes after all the other
# code in try, except, and else blocks regardless of
# whether an exception was raised or not.




# The Python programming language requires us to order except blocks from most specific at the 
# top to least specific (most general) at the bottom.


# There are many types of exceptions in Python, but there are only seven types that your code will need to handle in CSE 111, namely:

# TypeError
# ValueError
# ZeroDivisionError
# IndexError
# KeyError
# FileNotFoundError
# PermissionError