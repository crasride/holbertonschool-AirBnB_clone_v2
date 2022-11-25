#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
# task 6
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import models
# from models import storage


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # task 6
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        self.updated_at = datetime.now()
        # task 6
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        if "_sa_instance_state" in dictionary.keys():
            del dictionary["_sa_instance_state"]
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # task 6
        return dictionary

    # task 6
    def delete(self):
        """ Delete current instance from storage """
        models.storage.delete(self)
