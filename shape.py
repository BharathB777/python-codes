class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return 3.14 * self.radius * self.radius


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculateArea(self):
        return self.length * self.width


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculateArea(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(8, 3)
]

for shape in shapes:
    print(shape.calculateArea())