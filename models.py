import random
import string

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))


class User(Base):
    __tablename__ = 'user'

    def __iter__(self):
        _dict = self.__dict__
        _new_dict = {key: value for key, value in _dict.items()
                     if key is not '_sa_instance_state'}
        return _new_dict.iteritems()

    id = Column(Integer, primary_key=True)
    password_hash = Column(String(64))
    email = Column(String, index=True, nullable=False)
    picture = Column(String)
    requests = relationship("Request", cascade="delete")

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, passsword):
        return pwd_context.verify(passsword, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user_id = data['id']
        return user_id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'picture': self.picture
        }


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


class Proposal(Base):
    __tablename__ = 'proposal'

    def __iter__(self):
        _dict = self.__dict__
        _new_dict = {key: value for key, value in _dict.items()
                     if key is not '_sa_instance_state'}
        return _new_dict.iteritems()

    id = Column(Integer, primary_key=True)
    user_proposed_to = Column(Integer, nullable=False)
    user_proposed_from = Column(Integer, nullable=False)
    request_id = Column(Integer, ForeignKey('request.id'), nullable=False)
    filled = Column(Boolean)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_proposed_to': self.user_proposed_to,
            'user_proposed_from': self.user_proposed_from,
            'request_id': self.request_id,
            'filled': self.filled
        }


class MealDate(Base):
    __tablename__ = 'mealdate'

    def __iter__(self):
        _dict = self.__dict__
        _new_dict = {key: value for key, value in _dict.items()
                     if key is not '_sa_instance_state'}
        return _new_dict.iteritems()

    id = Column(Integer, primary_key=True)
    user_1 = Column(String, nullable=False)
    user_2 = Column(String, nullable=False)
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


engine = create_engine('sqlite:///meetneat.db')

Base.metadata.create_all(engine)
