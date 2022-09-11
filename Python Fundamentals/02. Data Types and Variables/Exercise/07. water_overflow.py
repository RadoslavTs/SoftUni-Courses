number_of_fills = int(input())
pouring_quantity = 0
total_quantity_filled = 0
for sequence in range(1, number_of_fills + 1):
    pouring_quantity = int(input())
    total_quantity_filled += pouring_quantity
    if total_quantity_filled > 255:
        print("Insufficient capacity!")
        total_quantity_filled -= pouring_quantity
print(total_quantity_filled)