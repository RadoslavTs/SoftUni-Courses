show_name = input()
season_count = int(input())
episodes_count = int(input())
episode_length = float(input())
ads_length = episode_length * 0.2
episode_with_ads = episode_length + ads_length
special_time = season_count * 10
total_watch_time = episode_with_ads * episodes_count * season_count + special_time
print(f"Total time needed to watch the {show_name} series is {total_watch_time:.0f} minutes.")