"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
                                    220 - age = max_heart_rate_per_min 
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your hearts maximum rate.
"""



MAX_BEATS_PER_MINUTE = 220


def range_heart_rate(age:int) -> tuple[int,int]:
    # First get the range which is 220 - age
    # Then find 65% and 85% of that number
    user_age_range = MAX_BEATS_PER_MINUTE - age
    min_heart_rate = int(user_age_range * .65)
    max_heart_rate = int(user_age_range * .85) 
    # Return the two values
    return min_heart_rate, max_heart_rate

    
user_age = int(input("Please enter your age: "))
# Take the two values and equal them to the two out puts from the function
min_heart_rate, max_heart_rate = range_heart_rate(user_age)
# Print using fstring to get both values in nicely 
print(f"""
When you exercise to strengthen your heart, you should
keep your heart rate between {min_heart_rate} and {max_heart_rate} beats per minute.
          """)

# > python heart_rate.py
# Please enter your age: 23
# When you exercise to strengthen your heart, you should
# keep your heart rate between 128 and 167 beats per minute.