# Benjamin Strong, CSE111, Sept. 9, 2025
# So This one was a dewsy...
# I have found out that I struggle to work with structure and code that I didn't write, so using functions given to me 
# just makes me go, "What am I suppose to do with this", but I got it working!
# Things I added:
# A password list to remember what passwords you entered, at the end of the program, it will tell you what you tried
# Also it tells you if you already tried something. Also if you add nothing, just a space the program will tell you. 
# Asked ChatGPT to help me with suggesting to add to passwords, now if you put in a pass word it will suggest some 
# improvements and tell you if the password is great as well. 
# I also made sure to add all the types to everything hah.
# Added a max length of 30, cuz thats just doin' too much. I hope this is okay.
# To be honest I tried to just get ChatGPT to write this all for me... but it made me more confused so I HAD to write it myself
# guess AI isn't that smart yet... or i'm just too dumb... oh well! 


LOWER:list[str]=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", 
       "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER:list[str]=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
       "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS:list[str]=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL:list[str]=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", 
         "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "?", "/", "`", "~"]

password_list:list[str] = []

def main():
    """Provides the user input loop. The loop asks the user for a password to test. If that password is anything but "q" or 
    "Q" call the password_strength function and report the results to the user. If the user enters "q" or "Q", 
    quit the program."""
    user_pass = ""
    while user_pass.lower() != "q":
        user_pass = input("What is your password? (q to quit): ")
        if user_pass in password_list:
            print("Already tried this one buddy.")
        elif user_pass.lower() == "q":
            break
        else:
            password_list.append(user_pass)
            print(password_strength(user_pass))
    print("\nPasswords tried:")
    for item in password_list:
        print(" -", item)
            

def word_in_file(word:str, filename:str, case_sensitive:bool=False) -> bool: 
        """This function reads a file (specified by the filename parameter) in which each line of the file contains a single word. 
        If the word passed in the word parameter matches a word in the file the function returns a true otherwise it returns a 
        false. If the parameter case_sensitive is true a case sensitive match is performed. If case_sensitive is false 
        a case insensitive match is performed. The case_sensitive parameter should default to False"""
        with open(filename, "r",encoding="utf-8") as file:
            for line in file:
                cln_line = line.strip()
                if case_sensitive == False:
                    if word.lower() == cln_line.lower():
                        return True
                else:
                    if word == cln_line:
                        return True
        return False
    
def word_has_character(word:str, character_list:list[str]) -> bool: 
    """This function loops through each character in the string passed in the word parameter to see if that character is 
    in the list of characters passed in the character_list parameter. If any of the characters in the word are present in 
    the character list return a true, If none of the characters in the word are in the character list return false"""
    for letter in word:
        if letter in character_list:
            return True
    return False
def word_complexity(word:str) -> int: 
    """This function creates a numeric complexity value based on the types of characters the word parameter contains. 
    One point of complexity is given for each type of character in the word. The function calls the word_has_character 
    function for each of the 4 kinds of characters (LOWER, UPPER, DIGITS, SPECIAL). If the word has that kind of character 
    a point is added to complexity rating. Since there are 4 kinds of characters the complexity rating will range from 0 
    to 4. (0 would be returned only if word contained no characters or only contains characters that are not in any of the 
    lists.)"""
    
    # How it looked before:
    # complexity_score = 0
    # if word_has_character(word, LOWER):
    #     complexity_score +=1
    # if word_has_character(word,UPPER):
    #     complexity_score +=1
    # if word_has_character(word, DIGITS):
    #     complexity_score +=1
    # if word_has_character(word,SPECIAL):
    #     complexity_score +=1
    # return complexity_score


    # ChatGPT helped with this section 
    has_lower = word_has_character(word, LOWER)
    has_upper = word_has_character(word, UPPER)
    has_digits = word_has_character(word, DIGITS)
    has_special = word_has_character(word, SPECIAL)

    complexity_score = sum([has_lower, has_upper, has_digits, has_special])

    # Suggestions based on missing types
    suggestions:list[str] = []
    if not has_lower:
        suggestions.append("Add lowercase letters.")
    if not has_upper:
        suggestions.append("Add uppercase letters.")
    if not has_digits:
        suggestions.append("Add numbers.")
    if not has_special:
        suggestions.append("Add symbols (e.g., !, @, #, $).")
    if has_digits and has_lower and has_special and has_upper:
        print("This is a great password!")
    if has_upper and has_lower and has_digits and not has_special:
        print("This is a good password")

    if suggestions:
        print("Suggestions to make your password stronger:")
        for s in suggestions:
            print("  -", s)

    return complexity_score
def password_strength(password:str, min_length:int=10, strong_length:int=16, MAX_LENGTH:int = 30): 
    """This function checks length requirements, checks dictionary and known-passwords, calls word_complexity to calculate 
    the word's complexity then determines the password's strength based on the user requirements. It should print the 
    messages defined in the requirements and return the password's strength as a number from 0 to 5. The min_length 
    parameter should have a default value of 10. The strong_length parameter should have a default value of 16"""
    if word_in_file(password,"wordlist.txt") == True:
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, "toppasswords.txt", case_sensitive=True) == True:
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password.strip()) == 0:
        print("There's... there's nothing here. Try again.")
        return 0
    if len(password) >= MAX_LENGTH:
        print("This password is too long.")
        return 1
    elif len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password")
        return 5
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    
    complexity = word_complexity(password)

    if complexity == 1:
        return 2
    if complexity == 2:
        return 3
    if complexity == 3:
        return 4
    if complexity == 4:
        return 5
    else:
        return 1
        
if __name__ == "__main__":
    main()