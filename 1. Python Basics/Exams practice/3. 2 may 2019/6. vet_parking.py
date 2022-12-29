days_count = int(input())
hours_per_day = int(input())
total_cost = 0
daily_cost = 0
for daily_rate in range(1, days_count + 1):
    for hourly_rate in range(1, hours_per_day + 1):
        if daily_rate % 2 == 0 and hourly_rate % 2 != 0:
            total_cost += 2.5
            daily_cost += 2.5
        elif daily_rate % 2 != 0 and hourly_rate % 2 == 0:
            total_cost += 1.25
            daily_cost += 1.25
        else:
            total_cost += 1
            daily_cost += 1
    print(f"Day: {daily_rate} - {daily_cost:.2f} leva")
    daily_cost = 0
print(f"Total: {total_cost:.2f} leva")