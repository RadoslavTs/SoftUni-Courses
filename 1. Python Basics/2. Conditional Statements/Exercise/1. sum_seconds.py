first_player = int(input())
second_player = int(input())
third_player = int(input())
total_time = first_player + second_player + third_player
minutes = total_time // 60
seconds = total_time % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")