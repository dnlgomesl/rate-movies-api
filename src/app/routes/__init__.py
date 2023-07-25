from app.routes.status import status
from app.routes.movies import *


def define_routes(app):
    app.register_blueprint(status, url_prefix='/status/')
    app.register_blueprint(create, url_prefix='/movie/')