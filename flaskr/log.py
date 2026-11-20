from flask import Blueprint, render_template
from flaskr import message

log_bp = Blueprint("app_log",__name__)

@log_bp.route('/log/', defaults={'msg': 'index'})
@log_bp.get('/log/<msg>')
def robots(msg) :
    new_message = message.Message()
    new_message.content = str(msg)
    new_message.insert()
    return render_template('index.html')