from _collections import deque
customer_deque = deque()
command = input()
command_end = "End"
command_paid = "Paid"
while True:

    if command == command_paid:
        while customer_deque:
            print(customer_deque.popleft())

    elif command == command_end:
        print(f'{len(customer_deque)} people remaining.')
        customer_deque.append(command)
        break
    else:
        customer_deque.append(command)

    command = input()

