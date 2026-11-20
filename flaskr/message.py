from .flask_db import db

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer,primary_key= True)
    content = db.Column(db.String(64),unique= True)

    def insert(self):
        db.session.add(self)
        db.session.commit()
