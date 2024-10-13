import json
import os


MOVIES_FILE = "movies.json"

def get_movies():

    if os.path.exists(MOVIES_FILE):
        with open(MOVIES_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def save_movies(movies):

    with open(MOVIES_FILE, "w") as file:
        json.dump(movies, file, indent=4)

def add_movie(title, year, rating):

    movies = get_movies()
    movies[title] = {"year": year, "rating": rating}
    save_movies(movies)

def delete_movie(title):

    movies = get_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)

def update_movie(title, rating):

    movies = get_movies()
    if title in movies:
        movies[title]["rating"] = rating
        save_movies(movies)