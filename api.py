from fastapi import FastAPI
from services import get_movies, add_movie, delete_movie, get_movie_name
from pydantic import BaseModel

app = FastAPI()

class MovieCreate(BaseModel):
    name: str
    amount: float

class DeleteMovie(BaseModel):
    name: str

class GetMovieByName(BaseModel):
    name: str
    amount: int

@app.get("/movies")
def read_movies():
    movies = get_movies()
    if not movies:
        return "No movies in list"
    else:
        new_list = []
        for movie in movies:
            new_list.append(
                {
                    "name": movie.name,
                    "amount": movie.amount
                }
            )
        return new_list

@app.post("/movies")
def post_movies(movie: MovieCreate):
    new_movie = add_movie(movie.name, movie.amount)
    return {
        "message": "Movie added",
        "movie": {
        "name": new_movie.name,
            "amount": new_movie.amount
    }
    }

@app.delete("/movies/{name}")
def delete_movie_from_list(movie: DeleteMovie):
    delete = delete_movie(movie.name)
    return delete

@app.get("/movies/{name}")
def get_movie_by_name(name: str):
    movie = get_movie_name(name)

    return {
        "movie": {
            "name": movie.name,
            "amount": movie.amount
        }
    }
