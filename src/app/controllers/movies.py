from flask_api import status as flask_status
from app.util import make_response, make_error
from app.services.movie import create, get_by_id, get_all, update, delete, rating, get_one_note_rate_move
import pymongo


def post_movie(request):
    try:
        body = request.get_json()
        if "name" not in body or "director" not in body or "genre" not in body or "year" not in body or type(body["year"]) != int:
            return make_error(f'Something wrong happened: No valid attributes to create', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
        name = str(body["name"])
        director = str(body["director"])
        genre = str(body["genre"])
        year = body["year"]
        movie_created = create(name, director, genre, year)
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
        if "name" not in body and "director" not in body and "genre" not in body and "year" not in body and type(body["year"]) != int:
            return make_error(f'Something wrong happened: No valid attributes to update', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
        att = {}
        if "name" in body:
            att["name"] = str(body["name"])
        if "director" in body:
            att["director"] = str(body["director"])
        if "genre" in body:
            att["genre"] = str(body["genre"])
        if "year" in body:
            att["year"] = body["year"]
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
    try:
        body = request.get_json()
        if "rate" not in body or not (type(body["rate"]) == int or type(body["rate"]) == float) or body["rate"] > 10 or body["rate"] < 0:
            return make_error(f'Something wrong happened: No valid attributes to rate', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
        movie = rating(movie_id, body["rate"])
        return make_response(movie, flask_status.HTTP_202_ACCEPTED)
    except Exception as e:
       return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)

def not_rate_movie():
    try:
        movie = get_one_note_rate_move()
        return make_response(movie, flask_status.HTTP_200_OK)
    except Exception as e:
        return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
