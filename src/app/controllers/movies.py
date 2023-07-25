from flask_api import status as flask_status
from app.util import make_response, make_error
from app.services.movie import create
import pymongo
import sys


def post_movie(request):
    try:
        body = request.get_json()
        name = body["name"]
        director = body["director"]
        movie_created = create(name, director)
        return make_response(movie_created, flask_status.HTTP_201_CREATED)
    except pymongo.errors.DuplicateKeyError:
        return make_error(f'Something wrong happened: Duplicated Movie', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return make_error(f'Something wrong happened: {str(e)}', flask_status.HTTP_500_INTERNAL_SERVER_ERROR)