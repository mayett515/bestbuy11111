from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies_by_rating(self):
        pass

    @abstractmethod
    def add_movie(self):
        pass

    @abstractmethod
    def delete_movie(self):
        pass

    @abstractmethod
    def update_movie(self):
        pass

    @abstractmethod
    def print_random_key(self):
        pass



    @abstractmethod
    def search_movie(self):
        pass

    @abstractmethod
    def give_out_list(self):
        pass

    @abstractmethod
    def stats_movies(self):
        pass



