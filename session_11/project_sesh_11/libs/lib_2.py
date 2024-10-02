def what_are_we_doing(param_list_1):
    another_list = [item + " lovable" for item in param_list_1]
    print(another_list)


def generator_function(param1_list):
    for item in param1_list:
        yield "awww, what a lovely " + item + " whatever your heart desires"