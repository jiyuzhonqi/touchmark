from flask import Flask,render_template,make_response,jsonify
from .flask_db import db
from . import config
from . import views
from . import log


def create_app() ->Flask:
    app = Flask(__name__)
   
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = config.SQLALCHEMY_COMMIT_ON_TEARDOWN
    db.init_app(app)
    app.register_blueprint(views.bp)
    app.register_blueprint(log.log_bp)

    return app

app = create_app()

@app.route('/',methods=['GET','POST'])
def index():
    db.create_all()
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)