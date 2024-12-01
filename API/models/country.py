from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    cities = relationship("City", back_populates="country", cascade="all, delete-orphan")

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    @staticmethod
    def fromDict(data):
        if not isinstance(data, dict):
            raise ValueError("Se esperaba un diccionario")
        return Country(
            id=data.get('id'),
            name=data.get('name', data.get('nombre'))
        )

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.name,
            'ciudades': [city.to_dict() for city in self.cities] if self.cities else []
        }
