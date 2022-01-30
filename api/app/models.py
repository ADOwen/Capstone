from math import prod
from ntpath import join
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from secrets import token_hex

db = SQLAlchemy()
# create models based off of ERD (Database Tables)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    post = db.relationship('Post',backref='author', lazy=True)
    cart_item = db.relationship('Cart',backref='author', lazy=True)
    comments = db.relationship('Comment',backref='customer', lazy=True, passive_deletes=True)  
    likes = db.relationship('Like',backref='user', lazy=True, passive_deletes=True) 
    is_admin = db.Column(db.Boolean(), default =False)
    api_token = db.Column(db.String(32), default= None, nullable= True)

    def __init__(self, username, email, password,is_admin=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        self.api_token = token_hex(16)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'token': self.api_token
        }        

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    comments = db.relationship('Comment',backref='post', lazy=True, passive_deletes=True) 
    likes = db.relationship('Like',backref='post', lazy=True, passive_deletes=True)

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'date_created': self.date_created,
            'author': self.user_id,
            'comments': self.comments,
            'likes': self.likes,
        }

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)

    def __init__(self, text, user_id, post_id):
        self.text = text
        self.user_id = user_id
        self.post_id = post_id

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    price = db.Column(db.Float())
    image = db.Column(db.String())
    description = db.Column(db.String())
    created_on = db.Column(db.DateTime, default=datetime.now)
    cart_item = db.relationship('Cart',backref='cart_product', lazy=True)

    def __init__(self, name, price, image, description,created_on):
        self.name = name
        self.price = price
        self.image = image
        self.description = description
        self.created_on = created_on

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'price' : self.price,
            'image' : self.image,
            'description' : self.description,
            'created_on' : self.created_on,
        }

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete="CASCADE"), nullable=False)

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id
