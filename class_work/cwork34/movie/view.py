def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title}".center(50, "="))
            output = func(*args, **kwargs)
            print("=".center(50, "="))
            return output
        return wrap
    return wrapper


class MovieInterface:
    @add_title("Редактирование данных каталогов фильма")
    def get_user_answer(self):
        print("Действия с фильмами:"
              "\n1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        answer = input("Выберите вариант действия: ")
        return answer

    @add_title("Добавление фильма")
    def get_movie_info(self):
        dict_movie = {
            "название фильма": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_movie:
            dict_movie[key] = input(f"Введите {key}: ")
        return dict_movie

    @add_title("Каталог фильмов")
    def show_all_movies(self, movies):
        for ind, key in enumerate(movies, 1):
            print(f"{ind}. {key}")

    @add_title("Ввод названия фильма")
    def get_movie_name(self):
        movie_name = input("Ведите название фильма: ")
        return movie_name

    @add_title("Просмотр информации о фильме")
    def show_movie_info(self, movie_dict):
        for key in movie_dict:
            print(f"{key} - {movie_dict[key]}")

    @add_title("Сообщение об ошибке")
    def incorrect_movie_name(self, movie_name):
        print(f"Фильма с названием {movie_name} не существует!")

    @add_title("Удаление фильма")
    def show_remove_movie_name(self, movie):
        print(f"Фильм {movie} удален с каталога!")

    @add_title("Сообщение об ошибке")
    def incorrect_answer_error(self, user_answer):
        print(f"Введенное значение {user_answer} не корректно!")










