employees_happiness = list(map(int, input().split()))
happiness_improvement_factor = int(input())
happiness_multiplied = list(map(lambda x: x * happiness_improvement_factor, employees_happiness))
average_happiness = sum(happiness_multiplied) / len(happiness_multiplied)
above_average_happy = list(filter(lambda x: x > average_happiness, happiness_multiplied))
if len(above_average_happy) >= len(happiness_multiplied) / 2:
    print(f"Score: {len(above_average_happy)}/{len(happiness_multiplied)}. Employees are happy!")
else:
    print(f"Score: {len(above_average_happy)}/{len(happiness_multiplied)}. Employees are not happy!")