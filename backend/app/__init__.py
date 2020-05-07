from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

login = LoginManager(app)

from app import api