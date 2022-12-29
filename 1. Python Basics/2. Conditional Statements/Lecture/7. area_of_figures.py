from math import pi
type_of_the_figure = input()
result = 0
if type_of_the_figure == "square":
    side = float(input())
    result = side * side
elif type_of_the_figure == "rectangle":
    side_one = float(input())
    side_two = float(input())
    result = side_one * side_two
elif type_of_the_figure == "circle":
    radius = float(input())
    result = pi * radius * radius
elif type_of_the_figure == "triangle":
    triangle_side = float(input())
    triangle_height = float(input())
    result = (triangle_height * triangle_side) / 2
print(f"{result:.3f}")
