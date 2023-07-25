import hashlib
import json

from connect2db import DB

def generete_id(name, director):
    id_fields = {"name": name, "director": director}
    serialized = json.dumps(id_fields, separators=(',', ':'), sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(serialized.encode('utf-8')).hexdigest()

def create(name, director):
    id = generete_id(name, director)
    movie = {
        "_id" : id,
        "name": name,
        "director": name,
        "rating": 0,
        "count_rating": 0
    }

    DB.movie.insert_one(movie)

    return movie


def get_by_id(id):
    query = {"_id": id}
    movie = DB.movie.find_one(query)
    return movie

def get_by_name(name):
    query = {"name": name}
    movie = DB.movie.find_one(query)
    return movie

def get_all():
    movies = DB.movie.find({})
    return list(movies)

def update(movie_id, att):
    DB.movie.update_one({"_id": movie_id}, {"$set": att})

def remove_movie(id):
    query = {"_id": id}
    deleted_movie = DB.movie.delete_one(query)
    return deleted_movie.deleted_count