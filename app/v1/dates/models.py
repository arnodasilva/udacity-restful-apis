from sqlalchemy import Column, Integer, String

from app.v1.utils.database_provider import Base


class Date(Base):
    __tablename__ = 'mealdate'

    def __iter__(self):
        _dict = self.__dict__
        _new_dict = {key: value for key, value in _dict.items()
                     if key is not '_sa_instance_state'}
        return _new_dict.iteritems()

    id = Column(Integer, primary_key=True)
    user_1 = Column(Integer, nullable=False)
    user_2 = Column(Integer, nullable=False)
    restaurant_name = Column(String, nullable=False)
    restaurant_address = Column(String, nullable=False)
    restaurant_picture = Column(String)
    meal_time = Column(String, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_1': self.user_1,
            'user_2': self.user_2,
            'restaurant_name': self.restaurant_name,
            'restaurant_address': self.restaurant_address,
            'restaurant_picture': self.restaurant_picture,
            'meal_time': self.meal_time
        }
