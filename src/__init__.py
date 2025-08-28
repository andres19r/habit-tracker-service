from flask import Flask
import os
from .config.config import Config
from dotenv import load_dotenv
from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)

mongo = PyMongo(app)

config = Config().dev_config

app.config["ENV"] = config.ENV
app.config['MONGO_URI'] = 'mongodb://localhost:27017/myDatabase'
