def main():

#     fabrics:list[str] = []

#     fabrics.append('velvet')
#     fabrics.append('denim')

#     list1 = ["red", "orange", "yellow", "green", "blue"]
#     list2 = ["red", "orange", "green", "green", "blue"]

#     index = compare_lists(list1, list2)
#     if index == -1:
#         print("The lists are identical.")
#     else:
#         print(f"The lists differ at index {index}.")

# def compare_lists(list1: list[str], list2: list[str]) -> int:
#     length1 = len(list1)
#     length2 = len(list2)
#     limit = min(length1, length2)

#     i = 0
#     while i < limit:
#         element1 = list1[i]
#         element2 = list2[i]

#         if element1 != element2:
#             break
#         i += 1

#     if length1== length2 == i:
#         i = -1
#     return i

    # colors = ['red', 'blue', 'green', 'yellow', 'purple']

    # print("Original list:", colors)

    # length = len(colors)

    # print(f"The length of the list is: {length}")

    # print(f"The 3rd item in the list is: {colors[2]}")

    # colors[3] = 'orange'

    # print(f"Modified list: {colors}")


    # YEAR_PLANNED_INDEX = 0
    # HEIGHT_INDEX = 1
    # GIRTH_INDEX = 2
    # FRUIT_AMOUNT_INDEX = 3

    # apple_tree_data: list[list[float]] = [
    #     [2012, 2.7, 3.6, 70.5],
    #     [2012, 2.4, 3.7, 81.3],
    #     [2015, 2.3, 3.6, 62.7],
    #     [2016, 2.1, 2.7, 42.1]
    # ]
    # total_fruit_amount = 0

    # for inner_list in apple_tree_data:
    #     fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]
    #     print(f"Fruit amount: {fruit_amount}")
    #     total_fruit_amount += fruit_amount
    # print(f"Total fruit amount: {total_fruit_amount}")

    # one_tree = apple_tree_data[2]
    # height = one_tree[HEIGHT_INDEX]

    # print(f"Height: {height}")

    # x = 17
    # y = x
    # print(f"Before changing x: x {x}  y {y}")
    # x += 1
    # print(f"After changing x:  x {x}  y {y}")

    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x}  lx {lx}")
    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)
    print(f"After calling modify_args():  x {x}  lx {lx}")
def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")
    # Change the values of both parameters.
    n += 1
    alist.append(4)
    print(f"   After changing n and alist:  n {n}  alist {alist}")

if __name__ == "__main__":
    main()
    