from view import MovieInterface
from model import MovieModel


class MovieController:
    def __init__(self):
        self.movie_interface = MovieInterface()
        self.movie_model = MovieModel()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.movie_interface.get_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, user_answer):
        if user_answer == "1":
            new_movie = self.movie_interface.get_movie_info()
            self.movie_model.add_movie_info(new_movie)
        elif user_answer == "2":
            movies = self.movie_model.get_all_movies()
            self.movie_interface.show_all_movies(movies)
        elif user_answer == "3":
            movie_name = self.movie_interface.get_movie_name()
            try:
                movie_dict = self.movie_model.get_movie_info(movie_name)
            except KeyError:
                self.movie_interface.incorrect_movie_name(movie_name)
            else:
                self.movie_interface.show_movie_info(movie_dict)
        elif user_answer == "4":
            movie_name = self.movie_interface.get_movie_name()
            try:
                del_movie_name = self.movie_model.remove_movie(movie_name)
            except KeyError:
                self.movie_interface.incorrect_movie_name(movie_name)
            else:
                self.movie_interface.show_remove_movie_name(del_movie_name)
        elif user_answer == "q":
            self.movie_model.save_info()
        else:
            self.movie_interface.incorrect_answer_error(user_answer)





