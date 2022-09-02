control_minutes = int(input())
control_seconds = int(input())
length = float(input())
hundred_meter_seconds = float(input())
control_minutes_to_seconds = control_minutes * 60
control_total = control_seconds + control_minutes_to_seconds
delay_time = length / 120 * 2.5
martin_time = (length / 100) * hundred_meter_seconds - delay_time
difference = abs(control_total - martin_time)
if martin_time <= control_total:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {martin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")