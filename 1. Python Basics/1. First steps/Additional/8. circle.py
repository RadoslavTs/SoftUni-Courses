from math import pi
radius = float(input())
circle_area = pi * radius * radius
circle_perimeter = 2 * pi * radius
area_result = "{:.2f}".format(circle_area)
perimeter_result = "{:.2f}".format(circle_perimeter)
print(area_result)
print(perimeter_result)