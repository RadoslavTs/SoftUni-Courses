my_stack = list(input())
resulting_string = ''
while len(my_stack) > 0:
    element = my_stack.pop()
    print(element, end='')