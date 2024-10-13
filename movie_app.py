
from functions import stats_movies
import storage_json
from storage_json import StorageJson
from istorage import IStorage
from typing import Type
import os


class MovieApp:
    def __init__(self, storage: StorageJson):
        self._storage = storage
        self._dictionary = storage.file_path




    @staticmethod
    def _command_movie_stats():
        stats_movies()

    ...

    def generate_html(self):
        movies = self._dictionary
        # Start the HTML content with embedded CSS
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Movies Info</title>
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                }

                .movie-container {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                    gap: 20px;
                }

                .movie {
                    background-color: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    text-align: center;
                }

                .movie h2 {
                    margin-bottom: 10px;
                    font-size: 18px;
                }

                .movie p {
                    margin-bottom: 5px;
                    font-size: 14px;
                }

                .movie img {
                    margin-top: 10px;
                    width: 100%;
                    height: auto;
                    border-radius: 8px;
                }
            </style>
        </head>
        <body>
            <div class="movie-container">
        """

        # Dynamically generate movie blocks
        for movie, details in movies.items():
            poster = details.get("poster_url", "")
            rating = details.get("rating", "N/A")
            year = details.get("year", "N/A")

            # Each movie card with poster, rating, and year
            html_content += f"""
            <div class="movie">
                <h2>{movie}</h2>
                <p><strong>Rating:</strong> {rating}</p>
                <p><strong>Year:</strong> {year}</p>
                {'<img src="' + poster + '" alt="' + movie + ' Poster">' if poster else ''}
            </div>
            """

        # End the HTML content
        html_content += """
            </div>
        </body>
        </html>
        """

        # Write the generated HTML to a file
        with open("index.html", "w") as file:
            file.write(html_content)

        print("HTML file 'index.html' has been updated!")

    # Function to update the HTML
    def update_website(self):

        self.generate_html()

    def choose_function(self):
        #movies = self._storage.file_path
        print("\nMenu:")
        print("1. List movies with best rating from top to lowest rating bottom")
        print("2. Random movie")
        print("3. Add movie")
        print("4. Delete movie")
        print("5. Search movie")
        print("6. Update movie")
        print("7. Give out list")
        print("8. Stats of movies")
        print("9. Exit")
        print("10. Generate Website")
        choice = input("Select an option: ")
        if choice == "9":
            return False

        # Define a dictionary mapping keys to functions
        all_functions = {
            "1": self._storage.list_movies_by_rating,
            "2": self._storage.print_random_key,
            "3": self._storage.add_movie,
            "4": self._storage.delete_movie,
            "5": self._storage.search_movie,
            "6": self._storage.update_movie,
            "7": self._storage.give_out_list,
            "8": self._storage.stats_movies,
            "10": self.generate_html
            # "9": self._storage.exit_function
        }

        # Check if the choice is valid
        if str(choice) in all_functions:
            # Execute the chosen function
            all_functions[str(choice)]()
        else:
            print("Invalid option. Please try again.")



    def run(self):
        function_runs = True
        # Dictionary to store the movies and the rating
        movies = {

        }
        while function_runs:
            if self.choose_function() is False:
                print("Program successfully quit.")
                function_runs = False
            else:
                input("Press Enter to start the program again.")
        print("Have a nice day!")




