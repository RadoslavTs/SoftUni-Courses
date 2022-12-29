input_list = [item for item in input().split()]
sheep_number = 0
for sequence in range(len(input_list)):
    if input_list[sequence] == "wolf":
        print("Please go away and stop eating my sheep")
    elif input_list[sequence] == "wolf,":
        sheep_number = len(input_list) - sequence - 1
        print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
