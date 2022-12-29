from math import floor
ball_quantity = int(input())
scored_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
black_balls = 0
for sequence in range(ball_quantity):
    ball_color = input()
    if ball_color == "red":
        scored_points += 5
        red_balls += 1
    elif ball_color == "orange":
        scored_points += 10
        orange_balls += 1
    elif ball_color == "yellow":
        scored_points += 15
        yellow_balls += 1
    elif ball_color == "white":
        scored_points += 20
        white_balls += 1
    elif ball_color == "black":
        scored_points /= 2
        black_balls += 1
    else:
        other_balls += 1
print(f"Total points: {floor(scored_points):.0f}")
print(f"Red balls: {red_balls:.0f}")
print(f"Orange balls: {orange_balls:.0f}")
print(f"Yellow balls: {yellow_balls:.0f}")
print(f"White balls: {white_balls:.0f}")
print(f"Other colors picked: {other_balls:.0f}")
print(f"Divides from black balls: {black_balls:.0f}")