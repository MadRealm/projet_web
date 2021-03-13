from flask_sqlalchemy import SQLAlchemy
import yaml
import inspect
from flask import request
import base64
#from PIL import Image

db = SQLAlchemy()

def init_database():
    db.create_all()
    populate_database()


def populate_database():
    import database.models

    model_classes = [model_class for (model_name, model_class) in inspect.getmembers(database.models, inspect.isclass)]
    do_populate = sum([len(c.query.all()) for c in model_classes]) == 0

    if not do_populate:
        return
