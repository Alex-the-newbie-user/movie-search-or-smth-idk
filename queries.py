import time, sqlite3


class Film:
    def __init__(self, title, year, duration, rating, age_rating):
        self.title = title
        self.year = year
        self.duration = duration
        self.rating = rating
        self.age_rating = age_rating


def search_by_title(title: str) -> list[Film]:
    connection = sqlite3.connect("films.db")
    result = connection.execute(
        """
        SELECT title, year, duration, rating, age_rating FROM movies
        WHERE title LIKE ?;
    """,
        ["%" + title + "%"],
    )
    fetched_result = result.fetchall()
    return [Film(*film_data) for film_data in fetched_result]


def search_by_genre(genre: str) -> list[Film]:
    connection = sqlite3.connect("films.db")
    result = connection.execute(
        """
        SELECT title, year, duration, rating, age_rating FROM movies
        JOIN genres ON genres.id = movies.genre_id
        WHERE genres.name LIKE ?;
    """,
        ["%" + genre + "%"],
    )
    fetched_result = result.fetchall()
    return [Film(*film_data) for film_data in fetched_result]


def search_by_year_of_release(year: int) -> list[Film]:
    connection = sqlite3.connect("films.db")
    result = connection.execute(
        """
        SELECT title, year, duration, rating, age_rating FROM movies
        WHERE year = ?;
    """,
        [year],
    )
    fetched_result = result.fetchall()
    return [Film(*film_data) for film_data in fetched_result]


def search_by_rating(rating):
    connection = sqlite3.connect("films.db")
    result = connection.execute(
        """
        SELECT title, year, duration, rating, age_rating FROM movies
        WHERE rating > ?;
    """,
        [rating],
    )
    fetched_result = result.fetchall()
    return [Film(*film_data) for film_data in fetched_result]


def search_by_age_rating(age_rating):
    connection = sqlite3.connect("films.db")
    result = connection.execute(
        """
        SELECT title, year, duration, rating, age_rating FROM movies
        WHERE age_rating < ?;
    """,
        [age_rating],
    )
    fetched_result = result.fetchall()
    return [Film(*film_data) for film_data in fetched_result]


def show_every_movie():
    connection = sqlite3.connect("films.db")
    result = connection.execute("""
        SELECT title, year, duration, rating, age_rating FROM movies;
    """)
    fetched_result = result.fetchall()
    return [Film(*film_data) for film_data in fetched_result]
