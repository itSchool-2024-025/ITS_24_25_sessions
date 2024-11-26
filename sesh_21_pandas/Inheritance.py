class GeometricShape:
    def __init__(self, num_attr):
        self.num_attr = num_attr

    @staticmethod
    def addition():
        print("Luke, I am your Father!")

class Circle(GeometricShape):
    def __init__(self, name, num_attr):
        super().__init__(num_attr=num_attr)
        self.name = name

    @staticmethod
    def addition():
        print("... circle")


if __name__ == "__main__":
    GeometricShape.addition()
    geo_sh1 = GeometricShape(10)
    Circle.addition()
    circ1 = Circle(12, "circle")
    print(circ1.name)
    print(circ1.num_attr)
