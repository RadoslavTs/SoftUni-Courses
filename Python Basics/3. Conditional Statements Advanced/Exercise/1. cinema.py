projection_type = input()
rows = int(input())
columns = int(input())
profit = float()
available_seat = rows * columns
if projection_type == "Premiere":
    profit = available_seat * 12
elif projection_type == "Normal":
    profit = available_seat * 7.5
elif projection_type == "Discount":
    profit = available_seat * 5
print(f"{profit:.2f} leva")