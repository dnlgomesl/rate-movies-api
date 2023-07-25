from flask_api import status as flask_status
from app.util import make_response, make_error
from app.services.movie import create, get_by_id, get_all, update, delete, rating
import pymongo
import sys


def post_movie(request):
    try:
        body = request.get_json()
        if "name" not in body or "director" not in body or "genre" not in body:
            return make_error(f'Something wrong happened: No valid attributes to create', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
        name = body["name"]
        director = body["director"]
        genre = body["genre"]
        movie_created = create(name, director, genre)
        return make_response(movie_created, flask_status.HTTP_201_CREATED)
    except pymongo.errors.DuplicateKeyError:
        return make_error(f'Something wrong happened: Duplicated Movie', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_movie(movie_id):
    try:
        movie = get_by_id(movie_id)
        return make_response(movie, flask_status.HTTP_200_OK)
    except Exception as e:
        return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_movies():
    try:
        movies = get_all()
        return make_response(movies, flask_status.HTTP_200_OK)
    except Exception as e:
        return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def update_movie(movie_id, request):
    try:
        body = request.get_json()
        if "name" not in body and "director" not in body and "genre" not in body:
            return make_error(f'Something wrong happened: No valid attributes to update', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
        att = {}
        if "name" in body:
            att["name"] = body["name"]
        if "director" in body:
            att["director"] = body["director"]
        if "genre" in body:
            att["genre"] = body["genre"]
        movie = update(movie_id, att)
        return make_response(movie, flask_status.HTTP_202_ACCEPTED)
    except Exception as e:
        return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)

def delete_movie(movie_id):
    try:
        movie = delete(movie_id)
        return make_response(movie, flask_status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)

def rate_movie(movie_id, request):
    #try:
        body = request.get_json()
        if "rate" not in body or body["rate"] > 10 or body["rate"] < 0:
            return make_error(f'Something wrong happened: No valid attributes to rate', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
        movie = rating(movie_id, body["rate"])
        return make_response(movie, flask_status.HTTP_202_ACCEPTED)
    #except Exception as e:
    #   return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)