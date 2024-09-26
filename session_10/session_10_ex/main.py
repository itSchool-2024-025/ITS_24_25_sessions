def return_rest(int_number):
    if int_number%2 != 0:
        return True
    else:
        return False


def task_1_1():
    # Description:
    # Task: Use a lambda function inside the filter() function to extract all even numbers from a list.
    # * Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # even number = numar par
    # odd number = numar impar
    Input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_function = lambda param_1: True if param_1%2 == 0 else False
    # rest = return_rest(3)
    # print(rest)
    for number in Input:
        rest = my_function(number)
        # if rest == 0:
        # if rest == False:
        # if rest is False:
        # if rest is not True:
        if rest: # este opusul lui "if rest:" -> if rest == 1
            print(f"Number {number} is even, because rest is {rest}.")
        else:
            print(f"Number {number} is odd, because rest is {rest}.")
    even_numbers = filter(my_function, Input)
    print(list(even_numbers))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task_1_1()

