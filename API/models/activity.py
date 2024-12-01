from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(String(100), primary_key=True)
    name = Column(String(200))
    description = Column(Text)
    city_id = Column(Integer, ForeignKey('cities.id'))
    
    city = relationship("City", back_populates="activities")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city_id': self.city_id
        } 