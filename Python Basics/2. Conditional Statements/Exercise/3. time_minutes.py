hours = int(input())
minutes = int(input())
hours_in_minutes = hours * 60
total_time = hours_in_minutes + minutes
resulting_time = total_time + 15
resulting_hours = resulting_time // 60
resulting_minutes = resulting_time % 60
if resulting_hours == 24:
    resulting_hours = 0
if resulting_minutes < 10:
    print(f"{resulting_hours}:0{resulting_minutes}")
else:
    print(f"{resulting_hours}:{resulting_minutes}")