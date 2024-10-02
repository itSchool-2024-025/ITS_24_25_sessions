def my_awesome_function(param1_list):
    """
    This function will take each of the param param1_list elements and add 3 to it
    :return:
    """
    return_list = []
    for x in param1_list:
        try:
            return_list.append(x+3)
        except TypeError as e:
            print(f"An error has occured! {e}")
    return return_list

if __name__ == '__main__':
    print(my_awesome_function([12, 13, (True,), 3]))