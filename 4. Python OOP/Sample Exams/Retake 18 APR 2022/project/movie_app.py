from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        existing_user = ''
        try:
            existing_user = next(filter(lambda x: x.username == username, self.users_collection))
        except StopIteration:
            pass

        if existing_user:
            raise Exception("User already exists!")


        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        try:
            current_user = next(filter(lambda x: x.username, self.users_collection))
        except:
            raise Exception("This user does not exist!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        current_user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k, v in kwargs.items():
            if k == "title":
                movie.title = v
            elif k == 'year':
                movie.year = v
            elif k == "age_restriction":
                movie.age_restriction = v

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        current_user = ''
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        try:
            current_user = next(filter(lambda x: x.username, self.users_collection))
        except:
            pass
        self.movies_collection.remove(movie)
        current_user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        owner = next(filter(lambda x: x.username, self.users_collection))
        if movie in owner.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        owner.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = next(filter(lambda x: x.username, self.users_collection))
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        movies = {}
        for movie in self.movies_collection:
            movies[movie.year] = movie.details()

        movie_string = []
        for k, v in sorted(movies.items(), key=lambda x: x[0], reverse=True):
            movie_string.append(v)

        return '\n'.join(movie_string)

    def __str__(self):
        users = ''
        movies = ''
        if not self.users_collection:
            users = 'No users.'
        else:
            users = ', '.join(x.username for x in self.users_collection)
        if not self.movies_collection:
            movies = "No movies."
        else:
            movies = ', '.join(x.title for x in self.movies_collection)

        return f"All users: {users}\nAll movies: {movies}"