from datetime import datetime, timedelta
from collections import deque

robot_input = input().split(";")
robots = {}
detail_deque = deque()
for robot in robot_input:
    robot_name, robot_time = robot.split('-')
    if robot_name not in robots.keys():
        robots[robot_name] = []
    robots[robot_name].append(int(robot_time))
    robots[robot_name].append(0)

factory_time = datetime.strptime(input(), "%H:%M:%S")


detail = input()
while detail != 'End':
    detail_deque.append(detail)
    detail = input()

while detail_deque:
    factory_time += timedelta(0, 1)
    product = detail_deque.popleft()
    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1

    for name, value in robots.items():
        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        detail_deque.append(product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]


    # robot_dict = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robot_dict.items()}
    # free_robots = list(filter(lambda x: x[1][1] == 0, robot_dict.items()))
    #
    # if not free_robots:
    #     detail_deque.append(product)
    #     continue
    #
    # robot_dict[free_robots[0][0]][1] = free_robots[0][1][0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")
