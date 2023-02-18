from collections import deque

jobs = deque(input().split(', '))

job_index = int(input())

cycles = 0
while True:
    min_job = 10000
    for _ in range(len(jobs)):
        if jobs[_].isdigit():
            if int(jobs[_]) < min_job:
                min_job = int(jobs[_])
    next_index = jobs.index(str(min_job))
    cycles += int(jobs[next_index])
    jobs[next_index] = 'pass'
    if next_index == job_index:
        break


print(cycles)
