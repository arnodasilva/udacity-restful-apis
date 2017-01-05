import random
import string

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.v1.utils.database.database_provider import Base

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
