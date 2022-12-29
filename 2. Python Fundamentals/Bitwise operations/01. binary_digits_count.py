number_to_convert = int(input())
number_to_look_for = int(input())
resulting_number = []
count = 0
while number_to_convert > 0:
    remainer = number_to_convert % 2
    number_to_convert = number_to_convert // 2
    if int(remainer) == number_to_look_for:
        count += 1
print(count)