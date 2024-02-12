#!/usr/bin/env python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amnenity",
        "Place",
        "Review"
    ]
        
    def do_create(self, line):
        """ Creates an new instance """
        line_split = line.split(" ")
        if line == "":
            print(" ** class name missing **")
        elif line_split[0] not in HBNBCommand.__classes:
            print(" ** class doesn't exist")
        else:
            print(eval(line_split[0])().id)
            storage.save()

    def do_show(self, line):
        """ Prints the string repr of an instance based on the class name and id """
        line_split = line.split(" ")
        if line == "":
            print(" ** class name missing **")
        elif line_split[0] not in HBNBCommand.__classes:
            print(" ** class doesn't exist **")
        elif len(line_split) == 1:
            print(" ** instance id is missing **")
        else:
            objects = storage.all()
            try:
                print(objects["{}.{}".format(line_split[0], line_split[1])])
            except KeyError:
                print(" ** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        line_split = line.split(" ")
        if line == "":
            print(" ** class name missing **")
        elif line_split[0] not in HBNBCommand.__classes:
            print(" ** class doesn;t exist **")
        elif len(line_split) == 1:
            print(" ** instance id missing **")
        else:
            try:
                objects = storage.all()
                del objects["{}.{}".format(line_split[0], line_split[1])]
                storage.save()
            except KeyError:
                print(" ** no instance found **")

    def do_all(self, line):
        line_split = line.split(" ")
        objects = storage.all()
        if line == "":
            for valobj in objects.values():
                print(valobj)
        elif line_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist")
        else:
            for valobj in objects.values():
                if valobj.__class__.__name__ == line_split[0]:
                    print(valobj)

    def do_update(self, line):
        """ Updates an instance based on the class namee and id by adding or updating """
        objects = storage.all()
        line_split = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif line_split[0] not in HBNBCommand.__classes:
            print("**class doesn't exist **")
        elif len(line_split) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(line_split[0], line_split[1]) not in objects:
            print(" ** no instance found **")
        elif len(line_split) == 2:
            print("** attribute name missing **")
        elif len(line_split) == 3:
            print(" **value missing **")
        else:
            for object, value in objects.items():
                if "{}.{}".format(line_split[0], line_split[1]) == object:
                    value.__setattr__(line_split[2], line_split[3])
                    storage.save()


    def do_count(self, line):
        """ Retrieve the number of instances of a class """
        count = 0
        line
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True
    
    def do_EOF(self, line):
        """ EOF signal"""
        return self.do_quit()
    
    def do_nothing(self):
        pass

if __name__ == '__main__': 
    HBNBCommand().cmdloop()