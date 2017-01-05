from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.v1.utils.database.database_provider import Base


class Request(Base):
    __tablename__ = 'request'

    def __iter__(self):
        _dict = self.__dict__
        _new_dict = {key: value for key, value in _dict.items()
                     if key is not '_sa_instance_state'}
        return _new_dict.iteritems()

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    meal_type = Column(String, nullable=False)
    location_string = Column(String)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    meal_time = Column(String, nullable=False)
    filled = Column(Boolean)
    proposals = relationship("Proposal", cascade="delete")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'meal_type': self.meal_type,
            'location_string': self.location_string,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'meal_time': self.meal_time,
            'filled': self.filled
        }
