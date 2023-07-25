import hashlib
import json

from connect2db import DB

def create(name, director, genre):
    id = str(DB.movie.estimated_document_count())
    movie = {
        "_id" : id,
        "name": name,
        "director": director,
        "genre": genre,
        "rating": 0,
        "count_rating": 0
    }

    DB.movie.insert_one(movie)

    return movie


def get_by_id(id):
    query = {"_id": id}
    movie = DB.movie.find_one(query)
    if not movie:
        return {}
    return movie

def get_all():
    movies = DB.movie.find({})
    return list(movies)

def update(movie_id, att):
    DB.movie.update_one({"_id": movie_id}, {"$set": att})
    return get_by_id(movie_id)

def remove_movie(id):
    query = {"_id": id}
    DB.movie.delete_one(query)
    return get_by_id(id)
