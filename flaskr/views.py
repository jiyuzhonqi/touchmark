from flask import Blueprint
from flask import current_app
from werkzeug import Response

bp = Blueprint("core",__name__)

@bp.get('/text/robot.txt')
def robots() -> Response:
    return current_app.send_static_file('robot.txt')