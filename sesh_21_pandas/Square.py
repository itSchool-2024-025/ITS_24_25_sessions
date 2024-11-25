# Task1: Define a class named Square that will enable the user to instantiate objects from it
# Task2: Define a instance of the class Square and get its edge length
# Task3: Define a instance of the class Square and set its edge length to 10
# (Homework) Task4: Refactor the setter and getter methods using property decorators
# Define a classmethod that will get the name of the class

class Square:
    name = "Numele pe care vrem sa-l dam pentru Square"
    def __init__(self, edge_len):
        self.edge_len = edge_len

    def get_edge_len(self):
        return self.edge_len

    def set_edge_len(self, new_val):
        self.edge_len = new_val

    @classmethod
    def get_class_atr(cls):
        return cls.name

    @classmethod
    def set_class_atr(cls, new_val):
        cls.name = new_val

if __name__ == "__main__":
    square1 = Square(10)
    print(square1.get_edge_len())
    square1.set_edge_len(15)
    print(square1.get_edge_len())
    print(square1.get_class_atr())
    square1.set_class_atr("Square")
    print(square1.get_class_atr())