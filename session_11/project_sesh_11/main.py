
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    my_list = {1: "Alice", 2: "Fryja", 3: "Scadi", 4: "Athena", 5: "Baba"}
    print(type(my_list))
    # for item in my_list:
    #     print(item, end=" ")
    my_iter = iter(my_list.keys())
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))


def list_comprehension_funct(simple_list):
    my_list = [x for x in simple_list if x%2]
    for x in simple_list:
        # print(item)
        if x%2 == 1:
            my_list.append(x)
    print(my_list)


def what_are_we_doing(param_list_1):
    another_list = [item + " lovable" for item in param_list_1]
    print(another_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    list_1 = ["cat", "dog", "mouse"]
    list_comprehension_funct([1, 2, 3, 4, 5, 6])
    what_are_we_doing(list_1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
