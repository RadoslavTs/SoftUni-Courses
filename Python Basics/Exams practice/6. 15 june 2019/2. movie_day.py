movie_time = int(input())
scene_count = int(input())
scene_length = int(input())
terrain_prep = movie_time * 0.15
total_scene_time = scene_length * scene_count
total_time = total_scene_time + terrain_prep
difference = abs(movie_time - total_time)
if total_time > movie_time:
    print(f"Time is up! To complete the movie you need {difference:.0f} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {difference:.0f} minutes left!")