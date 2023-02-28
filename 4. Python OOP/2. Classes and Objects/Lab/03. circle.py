class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = (self.radius * self.radius) * self.pi
        return area

    def get_circumference(self):
        perimeter = 2 * self.pi * self.radius
        return perimeter


circle = Circle(15)
circle.set_radius(160)
# print(circle.get_area())
# print(circle.get_circumference())
