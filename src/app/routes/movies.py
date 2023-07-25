from flask import Blueprint, request
from flask_cors import cross_origin
from app.util import METHOD_NOT_DEFINED
from app.controllers import movies as controller

create = Blueprint('movie', __name__)

@create.route("", methods=["POST"])
@cross_origin(supports_credentials=True)
def main():
    if request.method == "POST":
        return controller.post_movie(request)
    
    return METHOD_NOT_DEFINED