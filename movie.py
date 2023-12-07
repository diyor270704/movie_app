import json
from json import JSONDecodeError


def get_all_movies():
    try:
        with open("movies.json") as f:
            all_m: list = json.load(f)
            f.close()
        return all_m
    except (JSONDecodeError, FileNotFoundError):
        with open("movies.json", "w") as f:
            json.dump([], f, indent=4)
            f.close()
        with open("movies.json") as f:
            all_m: list = json.load(f)
            f.close()
        return all_m


# adds movies to json
class Movie:
    def __init__(self, name, description, language, price):
        self.movie_name = name
        self.desc = description
        self.m_language = language
        self.price = price
        all_movies = get_all_movies()
        self.id = all_movies[-1]["id"] + 1 if len(all_movies) != 0 else 1

    def get_into_dict(self):
        movie = {
            "id": self.id,
            "name": self.movie_name,
            "description": self.desc,
            "language": self.m_language,
            "price": self.price
        }
        return movie

    def get_into_json(self):
        if not self.check_available():
            try:
                with open("movies.json") as f:
                    all_movies: list = json.load(f)
                    f.close()
                movie = self.get_into_dict()
                all_movies.append(movie)
                with open("movies.json", "w") as f:
                    json.dump(all_movies, f, indent=4)
                    f.close()
            except (FileNotFoundError, JSONDecodeError):
                with open("movies.json", "w") as f:
                    json.dump([], f, indent=4)
                    f.close()
                with open("movies.json") as f:
                    all_m: list = json.load(f)
                    f.close()
                movie = self.get_into_dict()
                return all_m.append(movie)
        else:
            print("movie already exists!")

    def check_available(self):
        all_movies = get_all_movies()
        for movie in all_movies:
            if movie['name'] == self.movie_name:
                return True
            else:
                return False
