from src.figure import Figure

PI = 3.141592653589793


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Circle radius must be greater than 0")
        self.radius = radius

    @property
    def area(self):
        return PI * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * PI * self.radius