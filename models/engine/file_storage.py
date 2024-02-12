#!/usr/bin/env python3

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        obj = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj, file, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, encoding='utf-8') as file:
                dictionary = json.load(file)
                for obj in dictionary.values():
                    cls_name = obj['__class__']
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError as e:
            return
        

