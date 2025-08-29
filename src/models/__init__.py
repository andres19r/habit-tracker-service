from flask_pymongo import PyMongo
from src import app

mongo = PyMongo(app)

db = mongo.db

users = db.users

habits = db.habits
