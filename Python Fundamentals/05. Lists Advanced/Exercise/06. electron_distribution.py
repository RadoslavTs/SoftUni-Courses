number_of_electrons = int(input())
current_shell = 0
resulting_list = []
while number_of_electrons > 0:
    current_shell += 1
    current_value = 2 * (current_shell * current_shell)
    if number_of_electrons >= current_value:
        number_of_electrons -= current_value
    else:
        current_value = number_of_electrons
        number_of_electrons -= current_value
    resulting_list.append(current_value)
print(resulting_list)

