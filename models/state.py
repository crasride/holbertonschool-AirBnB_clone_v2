#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel):
    """ State class """
    # Task 6
    __tablename__ = 'states'
    name = Column(String(128), nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')

    else:
        @property
        def cities(self):
            """return list of cities new"""
            list_city = []

            value = models.storage.all(City).values()
            for i in value:
                if self.id == i.state_id:
                    list_city.append(i)

            return list_city
