from _collections import deque

food_quantity = int(input())
order_deque = deque(list(map(int, input().split())))
biggest_order = max(order_deque)
print(biggest_order)
while order_deque:
    current_order = order_deque.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        order_deque.insert(0, current_order)
        break

if order_deque:
    orders_left = ''
    for order in order_deque:
        orders_left += str(order) + ' '
    print(f'Orders left: {orders_left}')
else:
    print('Orders complete')

#
# order_deque = deque([int(n) for n in input().split()])
# print(max(order_deque))
# for order in order_deque.copy():
#     if food_quantity - order >= 0:
#         order_deque.popleft()
#         food_quantity -= order
#     else:
#         print(f"Orders left: {' '.join([str(o) for o in order_deque])}.")
#         break
# else:
#     print("Orders complete")
