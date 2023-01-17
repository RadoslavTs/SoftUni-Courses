from collections import deque

pumps_quantity = int(input())
pump_list = deque([[int(x) for x in input().split()] for _ in range(pumps_quantity)])
tank_gas = 0
pump_list_copy = pump_list.copy()
index_result = 0

while pump_list_copy:
    gas, distance = pump_list_copy.popleft()
    tank_gas += gas
    if tank_gas - distance < 0:
        pump_list.rotate(-1)
        pump_list_copy = pump_list.copy()
        index_result += 1
        tank_gas = 0
    else:
        tank_gas -= distance


print(index_result)
