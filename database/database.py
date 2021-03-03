from flask_sqlalchemy import SQLAlchemy
import yaml
import inspect
from flask import request
import base64
#from PIL import Image

db = SQLAlchemy()

#img=open("C:\Users\simon\PycharmProjects\projet_web\Images\Arthropodes.jpg")
blob=base64.decodebytes(open("C:\\Users\\simon\\PycharmProjects\\projet_web\\Images\\Arthropodes.jpg", "rb").read())
print(type(blob))
print(blob)




def init_database():
    db.create_all()
    populate_database()


def populate_database():
    import database.models

    model_classes = [model_class for (model_name, model_class) in inspect.getmembers(database.models, inspect.isclass)]
    do_populate = sum([len(c.query.all()) for c in model_classes]) == 0

    if not do_populate:
        return
    '''
    with open("database/mock_data.yaml") as f:
        mock_data = yaml.load(f,Loader=yaml.SafeLoader)
        #mock_data = yaml.load(f)
        for mock_object_key, mock_object_dict in mock_data.items():
            if mock_object_key == "_classes":
                continue
            model_class_name = mock_object_dict.get("class")
            model_class = getattr(database.models, model_class_name)
            model_object = model_class()

            for attribute_name, attribute_name_value in mock_object_dict.items():
                if attribute_name=="image_data":
                    setattr(model_object, attribute_name, base64.decodebytes(open(attribute_name_value).read()))
                else:
                    setattr(model_object, attribute_name, attribute_name_value)

            db.session.add(model_object)
        db.session.commit()
    '''
