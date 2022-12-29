house_width = float(input())
house_length = float(input())
roof_height = float(input())
front_area = house_width * house_width - 1.2 * 2
back_area = house_width * house_width
left_side = house_length * house_width - 1.5 * 1.5
right_side = house_length * house_width - 1.5 * 1.5
green_area = front_area + back_area + left_side + right_side
green_paint_quantity = green_area / 3.4
roof_front = house_width * roof_height / 2
roof_back = roof_front
roof_left = house_width * house_length
roof_right = roof_left
red_area = roof_right + roof_back + roof_left + roof_front
red_paint_quantity = red_area / 4.3
result_green = "{:.2f}".format(green_paint_quantity)
result_red = "{:.2f}".format(red_paint_quantity)
print(result_green)
print(result_red)

