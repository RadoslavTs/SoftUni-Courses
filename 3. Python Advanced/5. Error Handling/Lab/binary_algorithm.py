def binary_algorithm(numbers, num):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle_index = (left + right) // 2
        middle_element = numbers[middle_index]
        if middle_element == num:
            return f"The required number is at {middle_index}"

        if num > middle_element:
            left = middle_index + 1
        else:
            right = middle_index - 1


input_list = list(map(int, input().split()))
value_to_look_for = int(input())
print(binary_algorithm(input_list, value_to_look_for))
