input_list = list(map(int, input().split()))
total_value = int()
resulting_list = []
for element in input_list:
    total_value += element
average_number = total_value / len(input_list)
for number in input_list:
    if number > average_number:
        resulting_list.append(number)
if len(resulting_list) == 0:
    print("No")
resulting_list = sorted(resulting_list, reverse=True)
resulting_list = resulting_list[0:5:]
resulting_string = list(map(str, resulting_list))
print(" ".join(resulting_string))
