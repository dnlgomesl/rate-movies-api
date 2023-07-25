from flask import Blueprint, request
from flask_cors import cross_origin
from app.util import METHOD_NOT_DEFINED
from app.controllers import movies as controller

create = Blueprint('create', __name__)

@create.route("", methods=["POST"])
@cross_origin(supports_credentials=True)
def rout_create():
    if request.method == "POST":
        return controller.post_movie(request)
    
    return METHOD_NOT_DEFINED

read_one = Blueprint('read_one', __name__)

@read_one.route("/movie/<movie_id>", methods=["GET"])
@cross_origin(supports_credentials=True)
def route_read_one(movie_id):
    if request.method == "GET":
        return controller.get_movie(movie_id)
    
    return METHOD_NOT_DEFINED

read_all = Blueprint('read_all', __name__)

@read_all.route("", methods=["GET"])
@cross_origin(supports_credentials=True)
def route_read_all():
    if request.method == "GET":
        return controller.get_movies()
    
    return METHOD_NOT_DEFINED

update = Blueprint('update', __name__)

@update.route("/movie/<movie_id>", methods=["PUT"])
@cross_origin(supports_credentials=True)
def route_update(movie_id):
    if request.method == "PUT":
        return controller.update_movie(movie_id, request)
    
    return METHOD_NOT_DEFINED

delete = Blueprint('delete', __name__)

@delete.route("/movie/<movie_id>", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def route_delete(movie_id):
    if request.method == "DELETE":
        return controller.delete_movie(movie_id)
    
    return METHOD_NOT_DEFINED