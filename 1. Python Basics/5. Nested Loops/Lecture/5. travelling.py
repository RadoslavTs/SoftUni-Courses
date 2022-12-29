destination = input()
accumulated_sum = 0
while destination != "End":
    budget = float(input())
    current_sum = float(input())
    accumulated_sum += current_sum
    while accumulated_sum < budget:
        current_sum = float(input())
        accumulated_sum += current_sum
    print(f"Going to {destination}!")
    accumulated_sum = 0
    destination = input()

