#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(
        String(128),
        nullable=False
        )
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete"
        )

    @property
    def cities(self):
        """
        Getter attribute cities that returns the list of 
        City instances with state_id equals to the current State.id
        """
        list_cities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                list_cities.append(city)
        return list_cities
