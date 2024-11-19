class MyClass:
    def __init__(self, color, no_of_windows):
        self.color = color
        self.hashtag_windows = no_of_windows
        print("Objected Created")

class AnotherClass:
    def __init__(self, attribute_value):
        self.attr = attribute_value

    def setter_method(self, new_value):
        self.attr = new_value

    def getter_method_my_attr(self):
        return self.attr

if __name__ == '__main__':
    # my_object = MyClass("blue", 2)
    # print(f"My object is {my_object.color}")
    # print(my_object.hashtag_windows)
    var = AnotherClass(attribute_value=12)
    print(var.attr)
    var.setter_method(2)
    print(var.getter_method_my_attr())
    print("-----------")
    var1 = AnotherClass(attribute_value=13)
    print(var1.attr)