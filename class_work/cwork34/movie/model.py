import pickle
import os.path


class Movie:
    def __init__(self, movie_name, genre, producer, release_year, duration, studio, actors):
        self.movie_name = movie_name
        self.genre = genre
        self.producer = producer
        self.release_year = release_year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.movie_name} ({self.producer})"


class MovieModel:
    def __init__(self):
        self.db_name = "movie_db.txt"
        self.movies = self.load_file()

    def add_movie_info(self, dict_movie):
        movie = Movie(*dict_movie.values())
        self.movies[movie.movie_name] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_movie_info(self, movie_name):
        movie = self.movies[movie_name]
        dict_movie = {
            "название фильма": movie.movie_name,
            "жанр": movie.genre,
            "режиссер": movie.producer,
            "год выпуска": movie.release_year,
            "длительность": movie.duration,
            "студия": movie.studio,
            "актеры": movie.actors
        }
        return dict_movie

    def remove_movie(self, movie):
        return self.movies.pop(movie)

    def save_info(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.movies, f)

    def load_file(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()




















