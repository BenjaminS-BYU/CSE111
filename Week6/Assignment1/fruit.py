def main():
    # Create and print a list named fruit_list.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"Original list: {fruit_list}")


    fruit_list.reverse()
    print(fruit_list)
    fruit_list.append("orange")
    print(fruit_list)
    fruit_list.remove("banana")
    print(fruit_list)
    fruit_list.remove("apple")
    print(fruit_list)
    fruit_list.insert(2, "cherry")
    print(fruit_list)
    popped = fruit_list.pop()
    print(f"Popped item: {popped}")
    print(fruit_list)
    fruit_list.sort()
    print(fruit_list)
    fruit_list.clear()
    print(fruit_list)


if __name__ == "__main__":
    main()