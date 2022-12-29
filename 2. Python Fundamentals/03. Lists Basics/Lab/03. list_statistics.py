number = int(input())
positive_list = []
negative_list = []
positives_count = 0
negatives_sum = 0
for sequence in range(number):
    current_number = int(input())
    if current_number > 0:
        positive_list.append(current_number)
        positives_count += 1
    else:
        negative_list.append(current_number)
        negatives_sum += current_number
print(positive_list)
print(negative_list)
print(f"Count of positives: {positives_count}")
print(f"Sum of negatives: {negatives_sum}")