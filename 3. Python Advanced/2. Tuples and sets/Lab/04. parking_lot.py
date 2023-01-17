command_count = int(input())
parking_lot = set()
for sequence in range(command_count):
    command, registration_number = input().split(", ")
    if command == "IN":
        parking_lot.add(registration_number)
    elif command == "OUT":
        parking_lot.remove(registration_number)
if not parking_lot:
    print("Parking Lot is Empty")
else:
    for car in parking_lot:
        print(car)