number_of_cars = int(input())
cars_dict = {}
for sequence in range(number_of_cars):
    car_input = input().split("|")
    car_type = car_input[0]
    car_mileage = int(car_input[1])
    car_fuel = int(car_input[2])
    if car_type not in cars_dict.keys():
        cars_dict[car_type] = [car_mileage, car_fuel]

command = input()
while command != "Stop":
    command_split = command.split(" : ")
    action = command_split[0]
    car = command_split[1]
    if car in cars_dict.keys():
        if action == "Drive":
            distance = int(command_split[2])
            fuel = int(command_split[3])
            if cars_dict[car][1] >= fuel:
                cars_dict[car][0] += distance
                cars_dict[car][1] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if cars_dict[car][0] >= 100000:
                    print(f"Time to sell the {car}!")
                    del cars_dict[car]
            else:
                print("Not enough fuel to make that ride")
        elif action == "Refuel":
            fuel = int(command_split[2])
            if fuel + cars_dict[car][1] > 75:
                refueled_amount = 75 - cars_dict[car][1]
                cars_dict[car][1] = 75
            else:
                refueled_amount = fuel
                cars_dict[car][1] += refueled_amount
            print(f"{car} refueled with {refueled_amount} liters")
        elif action == "Revert":
            decrease_amount = int(command_split[2])
            cars_dict[car][0] -= decrease_amount
            if cars_dict[car][0] < 10000:
                cars_dict[car][0] = 10000
            else:
                print(f"{car} mileage decreased by {decrease_amount} kilometers")

    command = input()

for cars in cars_dict.keys():
    print(f"{cars} -> Mileage: {cars_dict[cars][0]} kms, Fuel in the tank: {cars_dict[cars][1]} lt.")
