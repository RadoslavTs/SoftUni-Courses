from collections import deque

pizza_orders = deque(input().split(', '))
employees = deque(input().split(', '))

total_pizzas = 0

while pizza_orders and employees:
    current_order = int(pizza_orders.popleft())
    if current_order > 10 or current_order <= 0:
        continue
    current_employee = int(employees.pop())
    if current_order <= current_employee:
        total_pizzas += current_order
    else:
        current_order -= current_employee
        total_pizzas += current_employee
        pizza_orders.appendleft(str(current_order))

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    if employees:
        print(f"Employees: {', '.join(employees)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(pizza_orders)}")
