#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    # Task 6
    __tablename__ = 'states'
    name = Column(String(128), nullable=True)
    cities = relationship("City",  backref="state", cascade="delete")

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
