from connect2db import DB
from datetime import datetime
import hashlib
import json
import random

def generate_id(name, timestamp):
    id_fields = {"name": name, "timestamp":timestamp}
    serialized = json.dumps(id_fields, separators=(',', ':'), sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(serialized.encode('utf-8')).hexdigest()


def create(name, director, genre):
    id = generate_id(name, str(datetime.now()))
    movie = {
        "_id" : id,
        "name": name,
        "director": director,
        "genre": genre,
        "rating": 0,
        "count": 0
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

def delete(id):
    query = {"_id": id}
    DB.movie.delete_one(query)
    return get_by_id(id)

def rating(id, rate):
    movie = get_by_id(id)
    if "count" in movie and "rating" in movie:
        count = movie["count"] + 1
        rating_value = ((movie["rating"]*(count-1)) + rate) / count
        return update(id, {"rating": rating_value, "count": count})
    else:
        return {}

def get_one_note_rate_move():
    query = {"count": 0}
    movie = list(DB.movie.find(query))
    if len(movie) > 0:
        i = random.randint(0, len(movie)-1)
        return movie[i]
    return movie
