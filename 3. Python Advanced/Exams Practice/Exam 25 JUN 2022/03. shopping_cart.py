from collections import deque

def merge_the_tools(string, k):
    n = int(len(string) / k)
    deque_string = deque(list(string))
    final_result = ''
    final_string_result = ''

    for _ in range(n):
        resulting_word = []
        for p in range(k):
            current_letter = deque_string.popleft()
            if not resulting_word:
                resulting_word.append(current_letter)
            else:
                if current_letter not in resulting_word:
                    resulting_word.append(current_letter)

        letters = ''
        for let in resulting_word:
            letters += let
        final_result += f'{letters}\n'

    return final_result

input_string = 'AABCAAADA'
k_coef = 3

print(merge_the_tools(input_string, k_coef))