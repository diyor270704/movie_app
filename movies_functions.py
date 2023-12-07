import datetime
import json
from movie import Movie, get_all_movies
from json import JSONDecodeError


# adds movies to json file
def add_movie():
    name_of_movie = input("enter movie's name:")
    desc = input("write description about the movie:")
    language = input("enter language of the movie:")
    price = int(input("enter the price of the movie:"))
    price = str(price)
    price = price + '$'
    movie_obj = Movie(name_of_movie, desc, language, price)
    movie_obj.get_into_json()
    all_movies = get_all_movies()
    for movie in all_movies:
        if movie["name"] == name_of_movie and movie["description"] == desc:
            movie_id = movie["id"]
            print(f"your id is {movie_id}\nit will be needed to delete the movie")
            check_save = input("write 'yes' to save the id to json file to remember")
            if check_save == 'yes':
                pass


# gets like to movies
def get_like_to_movie(user_id):
    all_movies = get_all_movies()
    for movie in all_movies:
        print(movie)
        to_like = input("enter 'l' to like the movie: ")
        if to_like == 'l':
            if not is_liked(movie['id'], user_id):
                like = {
                    "movie_id": movie['id'],
                    "liked_who": user_id,
                    "liked_at": str(datetime.datetime.now())
                }
                with open("like.json") as f:
                    all_likes: list = json.load(f)
                    f.close()
                all_likes.append(like)
                with open("like.json", "w") as f:
                    json.dump(all_likes, f, indent=4)
                    f.close()
                print("thanks :)")
                print("next movie")
                check = input(
                    f"write yes if you want to buy this film\nthe price of this film stays for {movie['price']}")
                if check == 'yes' or check == 'Yes':
                    add_to_cart(movie['id'], user_id)
            else:
                print("you liked to this movie already")
                print("next movie")
                check = input(
                    f"write yes if you want to buy this film\nthe price of this film stays for {movie['price']}")
                if check == 'yes' or check == 'Yes':
                    add_to_cart(movie['id'], user_id)
        else:
            print("next movie")
            check = input(f"write yes if you want to buy this film\nthe price of this film stays for {movie['price']}")
            if check == 'yes' or check == 'Yes':
                add_to_cart(movie['id'], user_id)


# checks the is liked by same id
def is_liked(movie_id, liked_id):
    all_like = get_all_likes()
    k = 0
    for like in all_like:
        if like['movie_id'] == movie_id and like['liked_who'] == liked_id:
            return True
        else:
            k += 1
    if k == len(all_like):
        return False


# returns all data of like.json
def get_all_likes():
    try:
        with open("like.json") as f:
            all_like = json.load(f)
            f.close()
        return all_like
    except (FileNotFoundError, JSONDecodeError):
        with open("like.json", "w") as f:
            json.dump([], f, indent=4)
            f.close()
        with open("like.json") as f:
            all_like: list = json.load(f)
            f.close()
        return all_like


# adds movies to cart
def add_to_cart(movie_id, userid):
    all_movies = get_all_movies()
    k = 0
    for movie in all_movies:
        if check_bought(userid, movie['id']):
            if movie['id'] == movie_id:
                sold_movie = {
                    "id": movie_id,
                    "movie_price": movie['price'],
                    "sold_at": str(datetime.datetime.now()),
                    "bought": userid
                }
                with open("cart.json") as f:
                    all_carts: list = json.load(f)
                    f.close()
                all_carts.append(sold_movie)
                with open("cart.json", 'w') as f:
                    json.dump(all_carts, f, indent=4)
                    f.close()
                print("successfully added to cart thank you :)")
        else:
            k += 1
    if k == len(all_movies):
        print("something went wrong :(")


# returns all data of cart.json
def get_all_cart_data():
    try:
        with open("cart.json") as f:
            all_cart_data = json.load(f)
            f.close()
        return all_cart_data
    except (FileNotFoundError, JSONDecodeError):
        with open("cart.json", "w") as f:
            json.dump([], f, indent=4)
            f.close()
        with open("cart.json") as f:
            all_cart_data: list = json.load(f)
            f.close()
        return all_cart_data
# checks the user bought the movie before
def check_bought(userid, movie_id):
    all_data = get_all_cart_data()
    k = 0
    for cart in all_data:
        if cart['bought'] == userid and movie_id == cart['id']:
            return False
        else:
            k += 1
    if k == len(all_data):
        return True


# deletes movies
def delete_movie():
    id_movie = int(input("enter id to delete"))
    all_movies = get_all_movies()
    for movie in all_movies:
        if movie["id"] == id_movie:
            all_movies.remove(movie)
    with open("movies.json", "w") as f:
        json.dump(all_movies, f, indent=4)
        f.close()
