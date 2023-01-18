from collections import deque
from math import floor

impression_string = deque(input().split())
current_numbers = deque()
final_result = int()
counter = 0

while impression_string:
    current_character = impression_string.popleft()
    if current_character not in "*+-/":
        current_numbers.append(int(current_character))
    else:

        if current_character == "*" and current_numbers:
            if counter == 0:
                current_number = current_numbers.popleft()
            else:
                current_number = final_result
            while current_numbers:
                current_number *= current_numbers.popleft()
            final_result = current_number
            counter += 1

        elif current_character == "+" and current_numbers:
            if counter == 0:
                current_number = current_numbers.popleft()
            else:
                current_number = final_result
            while current_numbers:
                current_number += current_numbers.popleft()
            final_result = current_number
            counter += 1

        elif current_character == "-" and current_numbers:
            if counter == 0:
                current_number = current_numbers.popleft()
            else:
                current_number = final_result
            while current_numbers:
                current_number -= current_numbers.popleft()
            final_result = current_number
            counter += 1

        elif current_character == "/" and current_numbers:
            if counter == 0:
                current_number = current_numbers.popleft()
            else:
                current_number = final_result
            while current_numbers:
                current_number /= current_numbers.popleft()
            final_result = floor(current_number)
            counter += 1

print(floor(final_result))

