from app.routes.status import status
from app.routes.movies import *


def define_routes(app):
    app.register_blueprint(status, url_prefix='/status/')
    app.register_blueprint(create, url_prefix='/movie/')
    app.register_blueprint(read_one)
    app.register_blueprint(read_all, url_prefix='/movies/')
    app.register_blueprint(update)
    app.register_blueprint(delete)
