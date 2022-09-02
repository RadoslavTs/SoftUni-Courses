number = int(input())
printed = 1
flag = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        if printed > number:
            flag = True
            break
        print(str(printed) + " ", end = "")
        printed += 1
    if flag:
        break
    print("")