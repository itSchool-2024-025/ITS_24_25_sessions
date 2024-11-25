
class Circle:
    class_name = "Circle"

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_value):
        self.__radius = new_value

    @staticmethod
    def sum(a, b):
        return a+b

    @classmethod
    def get_class_atr(cls):
        return cls.class_name

    @classmethod
    def set_class_atr(cls, new_val):
        cls.class_name = new_val


if __name__ == '__main__':
    circle1 = Circle(10)
    # print(circle1.radius)
    # circle1.radius = 14
    # print(circle1.radius)
    # print(circle1.sum(12, 13))
    circle2 = Circle(11)
    print(circle1.class_name)
    print(circle2.class_name)
    circle1.set_class_atr("Square")
    print(circle1.get_class_atr())
    print(circle2.get_class_atr())
