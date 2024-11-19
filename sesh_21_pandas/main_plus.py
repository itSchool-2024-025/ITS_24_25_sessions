def return_my_name(my_name):
    prenume = "Smith"
    def join_names():
        return my_name+prenume
    return join_names

def return_a_bunch_of_number(func):
    return func(1, 2, 3, 4, 5)

def sum(*args):
    sum = 0
    for arg in args:
        sum = sum + arg
    return sum

def produce(*args):
    sum = 1
    for arg in args:
        sum = sum * arg
    return sum

def difference(*args):
    diff = 0
    for item in args[::-1]:
        diff = diff - item
    return diff

def addition(func):
    # print(func)
    print("debug 1")
    def nested_function(*args):
        print("debug 2")
        var = func(*args)
        print(var)
    return nested_function

@addition
def return_a_list_of_numbers():
    print("debug 0")
    return [1, 2, 3, 4, 5]

if __name__ == "__main__":
    # print(return_my_name("Elena"))
    # var = return_my_name
    # var1 = return_my_name
    # print(var("Elena"))
    # print(var1("Diana"))
    # print(return_a_bunch_of_number(sum))
    # print(return_a_bunch_of_number(produce))
    # print(return_a_bunch_of_number(difference))
    # print(return_a_list_of_numbers())
    return_a_list_of_numbers()