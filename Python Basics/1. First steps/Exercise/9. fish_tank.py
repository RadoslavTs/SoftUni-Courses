length = int(input())
width = int(input())
height = int(input())
sand = float(input())
volume = length * width * height * 0.001
sand_quantity = volume * sand / 100
water_quantity = volume - sand_quantity
print(water_quantity)