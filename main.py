import time
import queries

SEARCH_BY_TITLE = 1
SEARCH_BY_GENRE = 2
SEARCH_BY_YEAR = 3
SEARCH_BY_RATING = 4
SEARCH_BY_AGE_RATING = 5
SHOW_EVERY_MOVIE = 6


def print_films(film_list: list[queries.Film]):
    if film_list:
        print(
            "Title                                                        Year  Duration  Rating  Age rating "
        )
        time.sleep(0.01)
        print("-" * 100)
        time.sleep(0.01)
        for film in film_list:
            print(
                film.title.ljust(60, " "),
                str(film.year).ljust(6, " "),
                str(film.duration or "-").ljust(8, " "),
                str(film.rating).ljust(7, " "),
                (str(film.age_rating or "0") + "+").ljust(11, " "),
            )
            time.sleep(0.01)
        time.sleep(5)
        print()
        time.sleep(0.01)


print("Добро пожаловать в программу поиска фильмов!")
time.sleep(0.01)
while True:
    print("Выберите вариант поиска:")
    time.sleep(0.01)
    print("1) По названию фильма")
    time.sleep(0.01)
    print("2) По жанру")
    time.sleep(0.01)
    print("3) По году")
    time.sleep(0.01)
    print("4) По рейтингу фильма")
    time.sleep(0.01)
    print("5) По возрастному рейтингу")
    time.sleep(0.01)
    print("6) Все фильмы")
    user_choice = int(input("Введите номер поиска (1-6): "))
    if user_choice == SEARCH_BY_TITLE:
        title_request = input("Введите название фильма: ")
        search_result = queries.search_by_title(title_request)
        if title_request:
            print_films(search_result)
        else:
            print(
                "Извините, но введите хотя бы один символ чтобы начать поиск, или введите '6' чтобы показать все фильмы"
            )
            time.sleep(3)
    elif user_choice == SEARCH_BY_GENRE:
        genre_request = input("Введите жанр: ")
        search_result = queries.search_by_genre(genre_request)
        if genre_request:
            print_films(search_result)
        else:
            print(
                "Извините, но введите хотя бы один символ чтобы начать поиск, или введите '6' чтобы показать все фильмы"
            )
            time.sleep(3)
    elif user_choice == SEARCH_BY_YEAR:
        year_of_release_request = input("Введите год выпуска: ")
        search_result = queries.search_by_year_of_release(year_of_release_request)
        if year_of_release_request:
            print_films(search_result)
        else:
            print(
                "Извините, но введите хотя бы один символ чтобы начать поиск, или введите '6' чтобы показать все фильмы"
            )
            time.sleep(3)
    elif user_choice == SEARCH_BY_RATING:
        rating_request = input("Введите рейтинг: ")
        search_result = queries.search_by_rating(rating_request)
        if rating_request:
            print_films(search_result)
        else:
            print(
                "Извините, но введите хотя бы один символ чтобы начать поиск, или введите '6' чтобы показать все фильмы"
            )
            time.sleep(3)
    elif user_choice == SEARCH_BY_AGE_RATING:
        age_rating_request = input("Введите возрастное ограничение: ")
        search_result = queries.search_by_age_rating(age_rating_request)
        if age_rating_request:
            print_films(search_result)
        else:
            print(
                "Извините, но введите хотя бы один символ чтобы начать поиск, или введите '6' чтобы показать все фильмы"
            )
            time.sleep(3)
    elif user_choice == SHOW_EVERY_MOVIE:
        rendered_result = queries.show_every_movie()
        print_films(rendered_result)
