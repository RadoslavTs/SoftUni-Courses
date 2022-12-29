number = int(input())
break_flag = False
for sequence in range(number):
    digit = int(input())
    if digit % 2 != 0:
        print(f"{digit} is odd!")
        break_flag = True
        break
if not break_flag:
    print("All numbers are even.")

