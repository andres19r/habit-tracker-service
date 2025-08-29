from flask import Flask
import os
from .config.config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_DB_URI')


config = Config().dev_config

app.config["ENV"] = config.ENV

import src.models
