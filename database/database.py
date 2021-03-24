from flask_sqlalchemy import SQLAlchemy
import yaml
import inspect
from flask import request
import base64
#from PIL import Image

db = SQLAlchemy()

def init_database():
    db.create_all()

