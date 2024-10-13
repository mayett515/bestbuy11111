from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

storage = StorageJson('movies3.json')
movie_app = MovieApp(storage)
movie_app.run()


