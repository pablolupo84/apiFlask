from flask import Flask

from .models import db

app=Flask(__name__)

def create_app(enviroment):
    app.config.from_object(enviroment)
    return app