from libs.lib import my_func
from libs.lib import print_hi
from libs.lib import list_comprehension_funct
from libs.lib_2 import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    list_1 = ["cat"] #, "dog", "mouse"]
    # list_comprehension_funct([1, 2, 3, 4, 5, 6])
    # what_are_we_doing(list_1)

    """
    Using the generator_function(), wait for a confirmation from the user, to get the next element
    from a given collection, and, if en error arises, prompt the user and exit the loop, without
    any "red text".
    """
    my_single_obj = generator_function(list_1)
    while True:
        var = input("Message to user")
        my_set = {"dog"}
        # if
        if var == "Yes":
            try:
                print(next(my_single_obj))
                my_set[0] = "mouse"
            except (StopIteration, ZeroDivisionError, TypeError) as e:
                print("Rwo-Oh!")
                print(f"An error occurred: {e}")
            else:
                print("Now this has to work!")
            finally:
                print("OOoooookay!")
        else:
            print("Bye!")
            break
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

