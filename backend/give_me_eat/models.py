# Data classes for the app

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#from appserver import login


db = SQLAlchemy()

# Restaurant - make a request to google maps API and then get the data back and return it as json to vue

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        )

#@login.user_loader
#def load_user(id):
#    return User.query.get(id)

# User

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.column(db.String(120))
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    



# Restaurants Visited

# Points
