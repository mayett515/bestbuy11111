import csv
import os
import statistics
import random
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

def read_csv(filepath):
    if os.path.exists(filepath):
        movies = {}
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies[row['name']] = {'rating': float(row['rating']), 'year': int(row['year'])}
        return movies
    else:
        return {}

def write_csv(filepath, movies_dict):
    with open(filepath, mode='w', newline='') as file:
        fieldnames = ['name', 'rating', 'year']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for name, data in movies_dict.items():
            writer.writerow({'name': name, 'rating': data['rating'], 'year': data['year']})

class StorageCsv:
    def __init__(self, file_path):
        self._file_path = file_path
        self._movies_dict = read_csv(file_path)

    @property
    def movies_dict(self):
        return self._movies_dict

    def give_out_list(self):
        movies = self._movies_dict
        print(f"So many movies in the dictionary: {len(movies)}")
        for key, value in movies.items():
            print(f"{key} and the rating is {value['rating']}")

    def add_movie(self):
        movies = self._movies_dict
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
                    if movie_data["title"] in movies:
                        print(f"'{movie_data['title']}' already exists in the database.")
                    else:
                        movies[movie_data["title"]] = {
                            "rating": float(movie_data["rating"]),
                            "year": int(movie_data["year"]),
                            "poster_url": movie_data["poster_url"]
                        }
                        print(f"Added '{movie_data['title']}' to the dictionary.")

                    # Save updated movie list to CSV
                    write_csv(self._file_path, movies)
                    return movies
                else:
                    print(f"Could not add '{movie_name}' to the database.")

            except ValueError:
                print("Invalid input. Please try again.")

            except ValueError:
                print("Invalid input. Please try again.")

    def delete_movie(self):
        movies = self._movies_dict
        movie_to_delete = input("Which movie do you want to delete? ").strip()

        if movie_to_delete in movies:
            del movies[movie_to_delete]
            print(f"The movie '{movie_to_delete}' has been deleted.")
            write_csv(self._file_path, movies)
        else:
            print("The movie was not found in the database.")

    def update_movie(self):
        movies = self._movies_dict
        movie_name = input("Enter the name of the movie you want to update: ")

        if movie_name in movies:
            new_rating = input("Enter the new rating for the movie: ")
            try:
                movies[movie_name]['rating'] = float(new_rating)
                print(f"The rating for '{movie_name}' has been updated to {new_rating}.")
                write_csv(self._file_path, movies)
            except ValueError:
                print("Invalid rating. Please enter a valid number.")
        else:
            print("Error: The movie does not exist in the database.")

    def list_movies_by_rating(self):
        movies = self._movies_dict
        sorted_movies = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)

        print(f"Total movies: {len(movies)}\n")
        for movie, details in sorted_movies:
            print(f"{movie} | Rating: {details['rating']}, Year: {details['year']}")

    def random_movie_output(self):
        movies = self._movies_dict
        if movies:
            random_movie = random.choice(list(movies.keys()))
            return random_movie
        return None

    def print_random_key(self):
        random_key = self.random_movie_output()
        if random_key:
            movie = self._movies_dict[random_key]
            print(f"{random_key} | Rating: {movie['rating']}, Year: {movie['year']}")
        else:
            print("No movies available.")

    def search_movie(self):
        movies = self._movies_dict
        user_search = input("What do you want to search for? ").upper()
        for name, details in movies.items():
            if user_search in name.upper():
                print(f"{name} | Rating: {details['rating']}, Year: {details['year']}")
                return
        print("Movie not found.")

    def stats_movies(self):
        movies = self._movies_dict
        print(f"Average rating: {self.average_rating()}")
        print(f"Median rating: {self.median_rating()}")
        print("Best rated movies:")
        for movie in self.best_movie():
            print(f"{movie} with rating {movies[movie]['rating']}")
        print("Worst rated movies:")
        for movie in self.worst_movie():
            print(f"{movie} with rating {movies[movie]['rating']}")

    def average_rating(self):
        ratings = [movie['rating'] for movie in self._movies_dict.values()]
        return statistics.mean(ratings) if ratings else 0

    def median_rating(self):
        ratings = [movie['rating'] for movie in self._movies_dict.values()]
        return statistics.median(ratings) if ratings else 0

    def best_movie(self):
        movies = self._movies_dict
        max_rating = max(movie['rating'] for movie in movies.values())
        return [name for name, details in movies.items() if details['rating'] == max_rating]

    def worst_movie(self):
        movies = self._movies_dict
        min_rating = min(movie['rating'] for movie in movies.values())
        return [name for name, details in movies.items() if details['rating'] == min_rating]
