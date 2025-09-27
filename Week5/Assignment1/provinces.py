province_list: list[str] = []

def main() -> None:
    """starts the program creates an empty list that will be updated with every function"""
    
    # Make the file path known for debugging
    text_file = "C:/Users/baggi/OneDrive - BYU-Pathway Worldwide/Desktop/Coding/BYU/CSE111/Week5/Assignment1/provinces.txt"
    updated_list: list[str] = read_file(text_file)
    updated_list = remove_elements(updated_list)
    updated_list = replace_elements(updated_list, "AB", "Alberta")
    count_of_element: int = count_element("Alberta", updated_list)
    count_of_other: int = count_element("AB", updated_list)
    print(updated_list)
    print(f"\n'Alberta' shows up {count_of_element} times in the updated list.")
    print(f"'AB' shows up {count_of_other} many times in the updated list.")

def read_file(filename) -> list[str]:
    """Read the file and print out each line into a list on separate elements
    returns the list"""
    try:
        # Open the file as file
        with open(filename) as file:
            # For each line of the file, add it to the global province list
            for element in file:
                clean_line: str = element.strip()
                province_list.append(clean_line)
    except FileNotFoundError:
        print(f"ERROR: File {filename} not found")
        exit()
    return province_list

def remove_elements(updated_list) -> list[str]:
    """takes the list from the read_file() and removes the first and last elements
    return new list"""
    if len(updated_list) > 0:
        updated_list.pop()
        updated_list.remove(updated_list[0])
    return updated_list

def replace_elements(list_, remove_element, insert_element)-> list[str]:
    """Takes an instance of a repeating element and replaces it with another element
    remove_element parm is the element to be removed and the insert_element is to be inserted
    returns the new list"""
    for element in list_:
        if element == remove_element:
            element_index: int = list_.index(remove_element)
            list_.insert(element_index, insert_element)
            list_.remove(remove_element)
    return list_

def count_element(element_num, list_) -> int:
    """Counts the number of a certain element returns the number of that count"""
    count = 0
    for element in list_:
        if element == element_num:
            count += 1
    return count



if __name__ == "__main__":
    main()






# Open the provinces.txt file for reading.
## with open file as province list


# Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
## elements_list

# Print the entire list.
# Remove the first element from the list.
# Remove the last element from the list.
# Replace all occurrences of "AB" in the list with "Alberta".
# Count the number of elements that are "Alberta" and print that number.