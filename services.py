from models import Movie
import json

try:
    with open("movies.json", "r") as file:
        data = json.load(file)
        movie_list = []
        for movie in data:
            m = Movie(movie["name"], movie["amount"])
            movie_list.append(m)
except FileNotFoundError:
    movie_list = []

def get_total_amount():
    total_spent = 0
    for movie in movie_list:
        total_spent += movie.amount
    return total_spent

def get_expensive_movies():
    expensive_movies = []
    for movie in movie_list:
        if movie.amount > 100:
            expensive_movies.append(movie)

    return expensive_movies

def add_movie():
    while True:
        name = input("Enter a name of a movie or type 'back' to enter main menu: ")
        if name == 'back':
            break
        while True:
            amount = input("Enter amount of ticket: ")
            try:
                amount = float(amount)
                movie = Movie(name, amount)
                movie_list.append(movie)
                break
            except ValueError:
                print("Please enter a valid number")

def get_movies():
    if not movie_list:
        return "No movies in the list\n"
    return movie_list

def get_movie_by_name():
    if not movie_list:
        return "There are no movies to show\n"
    matches = []
    name = input("Please enter the name of a movie: ")
    for movie in movie_list:
        if movie.name == name:
            matches.append(movie)
    if matches:
        return matches
    return f"{name} not found\n"

def delete_movie():
    if not movie_list:
        return "There are no movies to delete"
    name = input("Please enter the name of a movie to delete: ")
    new_list = []
    count = 0
    for movie in movie_list:
        if movie.name == name:
            count += 1
        else:
            new_list.append(movie)
    movie_list.clear()
    movie_list.extend(new_list)
    if count > 0:
        return f"{count} movies deleted from list"
    else:
        return "No movies removed from list"

def update_price():

    count = 0

    if not movie_list:
        return "There are no movies to update price"

    name = input("Please enter the name of a movie to update price: ")

    while True:
        new_amount = input("Enter the new price: ")
        try:
            new_amount = float(new_amount)
            break
        except ValueError:
            print("Please enter a valid number")

    for movie in movie_list:
        if movie.name == name:
            movie.amount = new_amount
            count += 1

    if count > 0:
        return f"updated {count} movie(s)"
    else:
        return "No movie found"

def average_movie_price():
    if not movie_list:
        return "No movies in list"
    total_price = 0
    for movie in movie_list:
        total_price += movie.amount
    average_price =  total_price / len(movie_list)
    return f"The average price of movies is {average_price:.2f}"

def lowest_price():
    if not movie_list:
        return "No movies in list"
    cheapest_movies = []
    min_price = movie_list[0].amount

    for movie in movie_list:
        if movie.amount < min_price:
            min_price = movie.amount

    for movie in movie_list:
        if movie.amount == min_price:
            cheapest_movies.append(movie)

    return cheapest_movies

def highest_price():
    if not movie_list:
        return "No movies in list"
    expensive_movies = []
    max_price = movie_list[0].amount

    for movie in movie_list:
        if movie.amount > max_price:
            max_price = movie.amount

    for movie in movie_list:
        if movie.amount == max_price:
            expensive_movies.append(movie)

    return expensive_movies

def save_movies():
    if not movie_list:
        movie_list.clear()
        with open("movies.json", "w") as f:
            json.dump(movie_list, f)
        return "No movies to save"
    data = []
    for movie in movie_list:
        data.append(
            {
                "name": movie.name,
                "amount": movie.amount
            }
        )

    with open("movies.json", "w") as f:
        json.dump(data, f)
    return "Movie list saved to file"
