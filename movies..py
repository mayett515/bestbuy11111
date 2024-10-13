import functions
import movie_storage




def choose_function():
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
