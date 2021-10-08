from flask import Flask
from config import Config

# from .movies.routes import movies -- imports blueprint for registration

app = Flask(__name__)


# app.register_blueprint(movies) -- registers blueprint

app.config.from_object(Config) # configures app from config.py

from . import routes