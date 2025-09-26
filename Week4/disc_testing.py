def main():    
    numbers_list = [1, 2, 3, 4, 5]

    names_list = ["Alice", "Bob", "Charlie"]

    student_dict = dict(zip(numbers_list, names_list))
    print(f"Dictionary: {student_dict}")
    print()

    for key, value in student_dict.items():
        print(f"Key: {key}, Value: {value}")

   

    # keys = list(student_dict.keys())
    # values = list(student_dict.values())

    # print(f"Keys: {keys}")
    # print(f"Values: {values}")

if __name__ == "__main__":
    main()