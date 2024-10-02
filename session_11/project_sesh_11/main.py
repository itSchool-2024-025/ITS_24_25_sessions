from libs.lib import my_func
from libs.lib import print_hi
from libs.lib import list_comprehension_funct
from libs.lib_2 import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    list_1 = ["cat", "dog", "mouse"]
    # list_comprehension_funct([1, 2, 3, 4, 5, 6])
    # what_are_we_doing(list_1)

    """
    Using the generator_function(), wait for a confirmation from the user, to get the next element
    from a given collection, and, if en error arises, prompt the user and exit the loop, without
    any "red text".
    """
    var = input("Message to user")
    my_single_obj = generator_function(list_1)
    print(type(my_single_obj))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
