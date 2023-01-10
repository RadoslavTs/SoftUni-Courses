data = input()
index_stack = []

for sequence in range(len(data)):
    ch = data[sequence]

    if ch == '(':
        index_stack.append(sequence)
    elif ch == ')':
        start_index = index_stack.pop()
        print(data[start_index: sequence + 1])

