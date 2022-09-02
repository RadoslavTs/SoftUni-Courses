movies_count = int(input())
highest_rating_movie = ""
highest_rating = 0
lowest_rating = 100
lowest_rating_movie = ""
total_rating = 0
for sequence in range(movies_count):
    movie_name = input()
    movie_rating = float(input())
    if movie_rating > highest_rating:
        highest_rating_movie = movie_name
        highest_rating = movie_rating
    if movie_rating < lowest_rating:
        lowest_rating_movie = movie_name
        lowest_rating = movie_rating
    total_rating += movie_rating
average_rating = total_rating / movies_count
print(f"{highest_rating_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")

