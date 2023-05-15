from typing import List

class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.strip() == "":
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        movies_liked = []
        owned_movies = []
        movies_liked_str = ''
        owned_movies_str = ''
        for movie in self.movies_liked:
            movies_liked.append(movie.details())
        for movie in self.movies_owned:
            owned_movies.append(movie.details())
        if not movies_liked:
            movies_liked_str = 'No movies liked.'
        else:
            movies_liked_str = '\n'.join(movies_liked)

        if not owned_movies:
            owned_movies_str = 'No movies owned.'
        else:
            owned_movies_str = '\n'.join(owned_movies)
        return f"Username: {self.username}, Age: {self.age}\n" \
               f"Liked movies:\n" \
               f"{movies_liked_str}\n" \
               f"Owned movies:\n" \
               f"{owned_movies_str}" \
