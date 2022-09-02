movie_name = input()
movie_number = 1
movie_score = 0
best_score = 0
best_movie = ""
while movie_name != "STOP":
    if movie_number == 7:
        break
    for sequence in range(len(movie_name)):
        letter_score = ord(movie_name[sequence])
        letter = movie_name[sequence]
        if letter.islower():
            letter_score -= (2 * len(movie_name))
        if letter.isupper():
            letter_score -= len(movie_name)
        movie_score += letter_score
        letter_score = 0

    if movie_score > best_score:
        best_score = movie_score
        best_movie = movie_name
    movie_score = 0
    movie_name = input()
    if movie_name != "STOP":
        movie_number += 1
if movie_number == 7:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {best_score} ASCII sum.")