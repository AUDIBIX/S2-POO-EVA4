from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'))
    
    country = relationship("Country", back_populates="cities")
    hotels = relationship("Hotel", back_populates="city")
    cars = relationship("Car", back_populates="city")
    activities = relationship("Activity", back_populates="city")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country_id': self.country_id,
            'hotels': [hotel.to_dict() for hotel in self.hotels],
            'cars': [car.to_dict() for car in self.cars],
            'activities': [activity.to_dict() for activity in self.activities]
        }
