list_of_integers = input().split()
command = input().split()
function_key = command[0]
maxeven_temp = 0
max_even_index = 0
while command[0] != "end":
    if function_key == "exchange":
        second_key = int(command[1])
        left_part = list_of_integers[second_key+1::]
        right_part = list_of_integers[0:second_key+1]
        list_of_integers.clear()
        for index_of_integers in range(len(left_part)):
            list_of_integers.append(left_part[index_of_integers])
        for index_of_integers_two in range(len(right_part)):
            list_of_integers.append(right_part[index_of_integers_two])
    if function_key == "max" and command[1] == "even":
        for maxeven in range(len(list_of_integers)):
            if int(list_of_integers[maxeven]) % 2 == 0:
                if int(list_of_integers[maxeven]) > maxeven_temp:
                    maxeven_temp = list_of_integers[maxeven]
                    max_even_index = maxeven
                    if list_of_integers.count(maxeven) > 1:
                        print(list_of_integers.index(maxeven_temp, maxeven + 1))
                    else:
                        print(list_of_integers.index(maxeven))
    command = input().split()
