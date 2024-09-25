
def print_hi(name):
    pass


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    print(f"This is my first list! {my_list}")
    # my_list_2 = [6, 7, 8, 9]
    # print(my_list+my_list_2)
    # print(my_list*3)
    my_tuple = (1, 2, 3, 4, 5, 3, 1, "straws", True, True)
    # print(f"This is my first tuple! {my_tuple}")
    #
    # print(my_tuple[0])
    # my_tuple_as_a_list = list(my_tuple)
    # # my_tuple_as_a_list[0] = 1
    # print(my_tuple_as_a_list)
    # my_tuple_as_a_list[0] = 10
    # print(my_tuple_as_a_list)
    # my_sec_tuple = tuple(my_tuple_as_a_list)
    # print(my_sec_tuple)
    # my_tuple = my_sec_tuple
    print(f"This is my first tuple! {my_tuple}")
    # print(f"Count method: {my_tuple.count(True)}")
    # print(23 in my_tuple)
    my_set = {"element1", "element2", "element3"}
    print(f"This is my first set! {my_set}")

    my_set_1 = {"element1", "element4", "element3", "element2"}
    print(my_set.intersection(my_set_1))
    print(my_set_1.intersection(my_set))

