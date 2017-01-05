from sqlalchemy import Column, Integer, Boolean
from sqlalchemy import ForeignKey

from app.v1.utils.database.database_provider import Base


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
