from flask import Flask
application = Flask(__name__)

# Set up URL's & functions
import random_meme
import specific_meme


@application.route('/')
def index():
    return "Services are up & running!"
