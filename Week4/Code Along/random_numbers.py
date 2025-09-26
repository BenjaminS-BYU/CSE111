import random

words:list[str] = ["dog", "cat", "frog", "bird", "pig", "yak", "python"]
word_list:list[str] = []

def main():
    num_amount = -1
    word_amount = -1
    while num_amount != 0 and word_amount != 0:
        num_amount = int(input("How many random numbers do you want to add? "))
        word_amount = int(input("How many words do you want to add? "))
    
        print(append_random_numbers([], num_amount))
        append_random_words(word_list, word_amount)
        print()
        print("One random number added:")
        print(append_random_numbers([]))
        

def append_random_numbers(numbers_list:list[int], quantity:int = 1) -> list[int]:
    for i in range(quantity):
        i = random.randrange(0,100)
        numbers_list.append(i)
    return numbers_list

def append_random_words(word_list:list[str], quantity:int = 1):
    for _ in range(quantity):
        word_list.append(random.choice(words))
    print(word_list)

if __name__ == "__main__":
    main()