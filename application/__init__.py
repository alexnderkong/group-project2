import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
logging.basicConfig(level=logging.DEBUG)
from os import getenv

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://groupproject:group-password@group-project.cs0cgwkolkmi.eu-west-1.rds.amazonaws.com/group-project'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey1234'
db = SQLAlchemy(app)
from application import routes