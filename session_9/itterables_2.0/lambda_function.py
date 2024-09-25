my_function = lambda param_1: param_1+1

def my_function_explicit(x):
    """
    The function will add 1 to the given parameter
    :param x:
    :return: sum of x +1
    """
    return x+1

def function_task_3_6():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # for value in my_list:
    #     print(my_function(value))

    print(list(map(lambda param_1: param_1+1, my_list)))

# function_task_3_6()

def function_task_3_2():
    numbers = [10, 15, 21, 30, 44, 53]
    odd_number = []
    # my_filter_function = lambda param_1: param_1%2
    for number in numbers:
        if number % 2 != 0:
            odd_number.append(number)
    print(odd_number)
    odd_numbers_1 = list(filter(lambda param_1: param_1%2, numbers))
    print(odd_numbers_1)

function_task_3_2()