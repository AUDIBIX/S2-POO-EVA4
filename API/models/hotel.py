from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(String(100), primary_key=True)
    name = Column(String(200), nullable=False)
    stars = Column(Integer)
    price_per_night = Column(Float)
    city_id = Column(Integer, ForeignKey('cities.id'))
    
    city = relationship("City", back_populates="hotels")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'stars': self.stars,
            'price_per_night': self.price_per_night,
            'city_id': self.city_id
        }
