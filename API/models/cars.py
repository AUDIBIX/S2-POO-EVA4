from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Car(Base):
    __tablename__ = 'cars'

    id = Column(String(100), primary_key=True)
    brand = Column(String(100))
    model = Column(String(100))
    type = Column(String(100))
    price_per_day = Column(Float)
    city_id = Column(Integer, ForeignKey('cities.id'))
    
    city = relationship("City", back_populates="cars")

    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'type': self.type,
            'price_per_day': self.price_per_day,
            'city_id': self.city_id
        }