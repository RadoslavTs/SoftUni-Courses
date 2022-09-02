number = input()
list_number = list(number)
resulting_list = []
for sequence in range(len(number)):
    resulting_list.append(max(list_number))
    list_number.remove(max(list_number))
resulting_string = [str(integer) for integer in resulting_list]
final_string = "".join(resulting_string)
result = int(final_string)
print(result)
# print(int(resulting_list))