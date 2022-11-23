#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

list_classes = {"State", "City", "Amenity", "User", "Place", "Review"}


class DBStorage():
    """
    New engine DBStorage
    Private class attributes
    """
    __engine = None
    __session = None

    def __init__(self):
        """Public instance methods, create the engine """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects by class name and should return a dictionary
        """
        new_dict = {}

        if cls:
            return self.get_data_from_table(cls, new_dict)

        for i in list_classes:
            new_dict = self.get_data_from_table(eval(i), new_dict)

        return new_dict

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session"""
        self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close session SQLAlchemy"""
        self.__session.close()
