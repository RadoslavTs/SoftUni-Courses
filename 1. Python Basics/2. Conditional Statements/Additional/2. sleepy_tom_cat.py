vacation_days = int(input())
work_days = 365 - vacation_days
work_days_play_time = 63 * work_days
vacation_days_play_time = 127 * vacation_days
real_play_time = vacation_days_play_time + work_days_play_time
difference = abs(30000 - real_play_time)
real_play_time_hours = difference // 60
real_play_time_minutes = difference % 60
if real_play_time < 30000:
    print("Tom sleeps well")
    print(f"{real_play_time_hours} hours and {real_play_time_minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{real_play_time_hours} hours and {real_play_time_minutes} minutes more for play")