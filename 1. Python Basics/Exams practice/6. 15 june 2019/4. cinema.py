theater_capacity = int(input())
entering_people = input()
total_income = 0
income_from_entering_people = 0
total_people_entered = 0
seats_left = theater_capacity
full_flag = False
negative_flag = False
while entering_people != "Movie time!":
    income_from_entering_people += int(entering_people) * 5
    if int(entering_people) % 3 == 0:
        income_from_entering_people -= 5
    if seats_left > int(entering_people):
        seats_left -= int(entering_people)
        total_income += income_from_entering_people
        income_from_entering_people = 0
    elif seats_left == int(entering_people):
        full_flag = True
        seats_left = 0
        total_income += income_from_entering_people
        income_from_entering_people = 0
    elif seats_left < int(entering_people):
        print("The cinema is full.")
        negative_flag = True
        income_from_entering_people = 0
        break
    entering_people = input()
if entering_people == "Movie time!":
    print(f"There are {seats_left} seats left in the cinema.")
print(f"Cinema income - {total_income:.0f} lv.")

