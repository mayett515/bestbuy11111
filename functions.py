"""Menu	Menu is displayed every time after running a command is executed.
-List movies
-Add movie
-Delete movie
-Update movie
-Stats	Average, Median, Best, Worst.
-Random movie
-Search movies	Case insensitive.
Movies sorted by rating	Descending order."""
import random
from random import choice
import statistics
import movie_storage

movies = {
    "The Shawshank Redemption": 9.5,
    "Pulp Fiction": 8.8,
    "The Room": 3.6,
    "The Godfather": 9.2,
    "The Godfather: Part II": 9.0,
    "The Dark Knight": 9.0,
    "12 Angry Men": 8.9,
    "Everything Everywhere All At Once": 8.9,
    "Forrest Gump": 8.8,
    "Star Wars: Episode V": 8.7
}


movies2 = {
    "The Shawshank Redemption": {
        "rating": 9.5,
        "year": 1994
    },
    "Pulp Fiction": {
        "rating": 8.8,
        "year": 1994
    },
    "The Room": {
        "rating": 3.6,
        "year": 2003
    },
    "The Godfather": {
        "rating": 9.2,
        "year": 1972
    },
    "The Godfather: Part II": {
        "rating": 9.0,
        "year": 1974
    },
    "The Dark Knight": {
        "rating": 9.0,
        "year": 2008
    },
    "12 Angry Men": {
        "rating": 8.9,
        "year": 1957
    },
    "Everything Everywhere All At Once": {
        "rating": 8.9,
        "year": 2022
    },
    "Forrest Gump": {
        "rating": 8.8,
        "year": 1994
    },
    "Star Wars: Episode V": {
        "rating": 8.7,
        "year": 1980
    }
}


def remove_braces_and_quotes(s):
    return s.replace('{', '').replace('}', '').replace('"', '').replace("'", '')


def exit_function(dict):
    return None


####this one just means list movies by rating
def list_movies():
    dict = movie_storage.get_movies()
    total_movies = str(len(dict))
    sorted_dict = sorted(dict.items(), key=lambda item: item[1]["rating"], reverse=True)

    print(f"{total_movies} movies in total\n")
    for each in sorted_dict:
        valueasstring = str(each[1])
        withoutbraces = remove_braces_and_quotes(valueasstring)
        print(f"{each[0]} | {withoutbraces}")

    print("")


###this one just gives out a list of the movies
def give_out_list():
    dict = movie_storage.get_movies()
    print("so much movies in dictionary : %d" % len(dict))
    for key, value in dict.items():
        print(f"{key} and the rating is {str(value["rating"])}")


def add_movie():
    movie_dict = movie_storage.get_movies()
    while True:
        try:
            name_rating = input("Please enter a movie name, a rating, and a year, separated by '#': ")

            if not name_rating:
                print("Please write like you were asked to do")
                continue
            movie_name, movie_rating_str, year = name_rating.split('#')

            if not movie_name.strip() or not movie_rating_str or not year.strip():
                print("Invalid input. Please try again.")
                continue
            try:
                movie_rating = float(movie_rating_str)
            except ValueError:
                print("invalid rating. Please enter a valid number.")
                continue
            if movie_name in movie_dict:
                print(f"'{movie_name}' already exists. Updating its information.")
            else:
                movie_dict[movie_name] = {"rating": movie_rating, "year": int(year)}

            print(f"Added '{movie_name}' to the dictionary.")
            movie_storage.save_movies(movie_dict)
            return movie_dict

        except ValueError:
            print("Invalid input. Please try again.")







def delete_movie():
    movie_dict = movie_storage.get_movies()
    movie_to_delete = input("Which movie do you want to delete? ").upper()

    for key in movie_dict.keys():
        if key.upper() == movie_to_delete:
            del movie_dict[key]
            print(f"The movie '{key}' has been deleted.")
            movie_storage.save_movies(movie_dict)
            return

    print("The movie was not found in the database.")


def update_movie_rating():
    dict = movie_storage.get_movies()
    movie_name = input("Enter the name of the movie you want to update: ")

    if movie_name in dict:

        new_rating = input("Enter the new rating for the movie: ")
        movie = dict[movie_name]
        movie['rating'] = float(new_rating)
        print(f"The rating for '{movie_name}' has been updated to {new_rating}.")
        movie_storage.save_movies(dict)
        return dict
    else:

        print("Error: The movie does not exist in the database.")


def random_movie_output():
    dict = movie_storage.get_movies()
    list_with_numbers = []
    first_nr = 0
    for key in dict:
        list_with_numbers.append(first_nr)
        first_nr = first_nr + 1
    dict_list = list(dict.keys())
    random_key = random.choice(dict_list)
    return random_key


def print_random_key():
    dict = movie_storage.get_movies()
    random_key = random_movie_output()

    print(f"{random_key} | Rating: {str(dict[random_key]["rating"])}")


"""here are functions for stats



 some"""


def median_rating():
    movie_dict = movie_storage.get_movies()
    ratings = []
    for movie in movie_dict.values():
        ratings.append(movie.get("rating", 0))
    return str(statistics.median(ratings))

    #     list_of_keys.append(key)
    #     list_of_values.append(value)
    # return str(statistics.median(list_of_values))


def average_rating():
    movie_dict = movie_storage.get_movies()
    ratings = []
    for movie in movie_dict.values():
        ratings.append(movie.get("rating", 0))
    return str(statistics.mean(ratings))


def best_movie():
    dict = movie_storage.get_movies()
    list_of_keys = []
    list_of_values = []
    movies_with_max_rating = []
    for movie in dict.values():
        list_of_values.append(movie.get("rating", 0))
    for movie in dict.keys():
        list_of_keys.append(movie)
    min_rating = max(list_of_values)
    for movie, value in dict.items():
        value = value.get("rating")
        if value == min_rating:
            movies_with_max_rating.append(movie)

    return movies_with_max_rating


def worst_movie():
    dict = movie_storage.get_movies()
    list_of_keys = []
    list_of_values = []
    movies_with_max_rating = []
    for movie in dict.values():
        list_of_values.append(movie.get("rating", 0))
    for movie in dict.keys():
        list_of_keys.append(movie)
    min_rating = min(list_of_values)
    for movie, value in dict.items():
        value = value.get("rating")
        if value == min_rating:
            movies_with_max_rating.append(movie)

    return movies_with_max_rating


def stats_movies():
    dict = movie_storage.get_movies()
    print(f"{average_rating()} | is the average rating")
    print(f"{median_rating()} | is the median rating")
    min_r_movies = worst_movie()
    max_r_movies = best_movie()
    print(f"best rated movies ")
    for movie in max_r_movies:
        print(f"{movie} with the rating {str(dict[movie].get("rating", 0))}")
    print(f"worst rated movies ")
    for movie in min_r_movies:
        print(f"{movie} with the rating {str(dict[movie].get("rating", 0))}")


def search_movie():
    dict = movie_storage.get_movies()
    user_search = input("What do you want to search for? ").upper()
    for key, value in dict.items():
        if user_search in key.upper():
            print(f"{key} and the rating is {(dict[key].get("rating", 0))} \n"
                  f" and the year of its release is {(dict[key].get("year", 0))} ")
            break
    else:
        print("Movie not found.")


