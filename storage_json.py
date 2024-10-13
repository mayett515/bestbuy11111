import json

from istorage import IStorage
import random
import statistics
import movie_storage
import json
import os
import requests
from typing import Optional


def fetch_movie_data(title: str) -> Optional[dict]:
    api_key = "cceb980f"
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["Response"] == "True":
            return {
                "title": data["Title"],
                "year": data["Year"],
                "rating": data["imdbRating"],
                "poster_url": data["Poster"]
            }
        else:
            print(f"Movie '{title}' not found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None


def get_movies(filepath):

    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            return json.load(file)
    else:
        return {}




def remove_braces_and_quotes(s):
    return s.replace('{', '').replace('}', '').replace('"', '').replace("'", '')

class StorageJson(IStorage):
    def __init__(self, file_path):
        self._file_path = get_movies(file_path)

    @property
    def file_path(self):
        return self._file_path






    def list_movies(self):
        dict = self._file_path
        print("so much movies in dictionary : %d" % len(dict))
        for key, value in dict.items():
            print(f"{key} and the rating is {str(value["rating"])}")
        ...

    # def add_movie(self):
    #     movie_dict = self._file_path
    #     while True:
    #         try:
    #             name_rating = input("Please enter a movie name, a rating, and a year, separated by '#': ")
    #
    #             if not name_rating:
    #                 print("Please write like you were asked to do")
    #                 continue
    #             movie_name, movie_rating_str, year = name_rating.split('#')
    #
    #             if not movie_name.strip() or not movie_rating_str or not year.strip():
    #                 print("Invalid input. Please try again.")
    #                 continue
    #             try:
    #                 movie_rating = float(movie_rating_str)
    #             except ValueError:
    #                 print("invalid rating. Please enter a valid number.")
    #                 continue
    #             if movie_name in movie_dict:
    #                 print(f"'{movie_name}' already exists. Updating its information.")
    #             else:
    #                 movie_dict[movie_name] = {"rating": movie_rating, "year": int(year)}
    #
    #             print(f"Added '{movie_name}' to the dictionary.")
    #             movie_storage.save_movies(movie_dict)
    #             return movie_dict
    #
    #         except ValueError:
    #             print("Invalid input. Please try again.")
    #     ...
    def add_movie(self):
        movie_dict = self._file_path
        while True:
            try:
                movie_name = input("Please enter a movie name: ")

                if not movie_name:
                    print("Please write like you were asked to do.")
                    continue

                # Fetch movie data from OMDb API
                movie_data = fetch_movie_data(movie_name)

                if movie_data:
                    # Check if movie already exists in the dictionary
                    if movie_data["title"] in movie_dict:
                        print(f"'{movie_data['title']}' already exists in the database.")
                    else:
                        movie_dict[movie_data["title"]] = {
                            "rating": float(movie_data["rating"]),
                            "year": int(movie_data["year"]),
                            "poster_url": movie_data["poster_url"]
                        }
                        print(f"Added '{movie_data['title']}' to the dictionary.")

                    # Save the updated movie list to JSON
                    movie_storage.save_movies(movie_dict)
                    return movie_dict
                else:
                    print(f"Could not add '{movie_name}' to the database.")

            except ValueError:
                print("Invalid input. Please try again.")


    def delete_movie(self):
        movie_dict = self._file_path
        movie_to_delete = input("Which movie do you want to delete? ").upper()

        for key in movie_dict.keys():
            if key.upper() == movie_to_delete:
                del movie_dict[key]
                print(f"The movie '{key}' has been deleted.")
                movie_storage.save_movies(movie_dict)
                return

        print("The movie was not found in the database.")
        ...

    def update_movie(self):
        dict = self._file_path
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

    def list_movies_by_rating(self):
        dict = self._file_path
        total_movies = str(len(dict))
        sorted_dict = sorted(dict.items(), key=lambda item: item[1]["rating"], reverse=True)

        print(f"{total_movies} movies in total\n")
        for each in sorted_dict:
            valueasstring = str(each[1])
            withoutbraces = remove_braces_and_quotes(valueasstring)
            print(f"{each[0]} | {withoutbraces}")

        print("")

    def random_movie_output(self):
        dict = self._file_path
        list_with_numbers = []
        first_nr = 0
        for key in dict:
            list_with_numbers.append(first_nr)
            first_nr = first_nr + 1
        dict_list = list(dict.keys())
        random_key = random.choice(dict_list)
        return random_key

    def print_random_key(self):
        dict = movie_storage.get_movies()
        random_key = self.random_movie_output()

        print(f"{random_key} | Rating: {str(dict[random_key]["rating"])}")

    def search_movie(self):
        dict = self._file_path
        user_search = input("What do you want to search for? ").upper()
        for key, value in dict.items():
            if user_search in key.upper():
                print(f"{key} and the rating is {(dict[key].get("rating", 0))} \n"
                      f" and the year of its release is {(dict[key].get("year", 0))} ")
                break
        else:
            print("Movie not found.")

    def stats_movies(self):
        dict = self._file_path
        print(f"{self.average_rating()} | is the average rating")
        print(f"{self.median_rating()} | is the median rating")
        min_r_movies = self.worst_movie()
        max_r_movies = self.best_movie()
        print(f"best rated movies ")
        for movie in max_r_movies:
            print(f"{movie} with the rating {str(dict[movie].get("rating", 0))}")
        print(f"worst rated movies ")
        for movie in min_r_movies:
            print(f"{movie} with the rating {str(dict[movie].get("rating", 0))}")

    def average_rating(self):
        movie_dict = self._file_path
        ratings = []
        for movie in movie_dict.values():
            ratings.append(movie.get("rating", 0))
        return str(statistics.mean(ratings))

    def median_rating(self):
        movie_dict = self._file_path
        ratings = []
        for movie in movie_dict.values():
            ratings.append(movie.get("rating", 0))
        return str(statistics.median(ratings))

    def best_movie(self):
        dict = self._file_path
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

    def worst_movie(self):
        dict = self._file_path
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

    def give_out_list(self):
        dict = self._file_path
        print("so much movies in dictionary : %d" % len(dict))
        for key, value in dict.items():
            print(f"{key} and the rating is {str(value["rating"])}")