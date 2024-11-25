class GeometricShape:
    def __init__(self, num_attr):
        self.num_attr = num_attr

    @staticmethod
    def addition():
        print("Luke, I am your Father!")

class Circle(GeometricShape):
    @staticmethod
    def addition():
        print("... circle")


if __name__ == "__main__":
    GeometricShape.addition()
    geo_sh1 = GeometricShape(10)
    Circle.addition()
    circ1 = Circle(12)
    print(circ1.num_attr)
