from movie_app import MovieApp
from storage_json import StorageJson
import movie_storage
import functions

def choose_function(storage):
    movies = movie_storage.get_movies()
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
    choice = input("Select an option: ")
    if choice == "9":
        return False

    # Define a dictionary mapping keys to functions
    all_functions = {
        "1": functions.list_movies,
        "2": functions.print_random_key,
        "3": functions.add_movie,
        "4": functions.delete_movie,
        "5": functions.search_movie,
        "6": functions.update_movie_rating,
        "7": functions.give_out_list,
        "8": functions.stats_movies,
        "9": functions.exit_function
    }

    # Check if the choice is valid
    if str(choice) in all_functions:
        # Execute the chosen function
        all_functions[str(choice)]()
    else:
        print("Invalid option. Please try again.")



def main():
    function_runs = True
    # Dictionary to store the movies and the rating
    movies = {
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
    while function_runs:
        if choose_function() is False:
            print("Program successfully quit.")
            function_runs = False
        else:
            input("Press Enter to start the program again.")
    print("Have a nice day!")



if __name__ == "__main__":
    main()