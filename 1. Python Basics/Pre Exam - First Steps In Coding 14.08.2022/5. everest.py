lodging = input()
height = 5364
days_climbing = 1
succeed_flag = False
while lodging != "END":
    climbed_height = int(input())
    if lodging == "Yes":
        days_climbing += 1
    if days_climbing > 5:
        break
    height += climbed_height
    if height >= 8848:
        succeed_flag = True
        break
    lodging = input()
if succeed_flag == True:
    print(f"Goal reached for {days_climbing} days!")
else:
    print("Failed!")
    print(f"{height}")
