from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Request, Proposal, MealDate

engine = create_engine('sqlite:///meetneat.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class DatabaseService:
    @staticmethod
    def getUsers():
        return session.query(User).all()

    @staticmethod
    def getUser(user_id):
        return session.query(User).filter_by(id=user_id).one()

    @staticmethod
    def addUser(user):
        session.add(user)
        session.commit()

    @staticmethod
    def updateUser(user_id, user_update):
        session.query(User).filter(id == user_id).update({
            User.email: user_update.email,
            User.email: user_update.picture
        })
        session.commit()

    @staticmethod
    def deleteUser(user_id):
        session.query(User).filter(id == user_id).delete()
        session.commit()

    @staticmethod
    def getRequests():
        return session.query(Request).all()

    @staticmethod
    def getRequest(request_id):
        return session.query(Request).filter_by(id=request_id).one()

    @staticmethod
    def addRequest(request):
        session.add(request);
        session.commit()

    @staticmethod
    def updateRequest(request_id, request_update):
        session.query(Request).filter(id == request_id).update({
            Request.meal_type: request_update.meal_type,
            Request.location_string: request_update.location_string,
            Request.latitude: request_update.latitude,
            Request.longitude: request_update.longitude,
            Request.meal_time: request_update.meal_time,
            Request.filled: request_update.filled
        })
        session.commit()

    @staticmethod
    def deleteRequest(request_id):
        session.query(Request).filter(id == request_id).delete()
        session.commit()

    @staticmethod
    def getProposals():
        return session.query(Proposal).all()

    @staticmethod
    def getProposal(proposal_id):
        return session.query(Proposal).filter_by(id=proposal_id).one()

    @staticmethod
    def addProposal(proposal):
        session.add(proposal)
        session.commit()

    @staticmethod
    def updateProposal(proposal_id, proposal_update):
        session.query(Proposal).filter(id == proposal_id).update({
            Proposal.user_proposed_to: proposal_update.user_proposed_to,
            Proposal.user_proposed_from: proposal_update.user_proposed_from,
            Proposal.request_id: proposal_update.request_id,
            Proposal.filled: proposal_update.filled
        })
        session.commit()

    @staticmethod
    def deleteProposal(proposal_id):
        session.query(Request).filter(id == proposal_id).delete()
        session.commit()

    @staticmethod
    def getDates():
        return session.query(MealDate).all()

    @staticmethod
    def getDate(date_id):
        return session.query(MealDate).filter_by(id=date_id).one()

    @staticmethod
    def addDate(date):
        session.add(date)
        session.commit()

    @staticmethod
    def updateDate(date_id, date_update):
        session.query(MealDate).filter(id == date_id).update({
            MealDate.user_1: date_update.user_1,
            MealDate.user_2: date_update.user_2,
            MealDate.restaurant_name: date_update.restaurant_update,
            MealDate.restaurant_address: date_update.restaurant_address,
            MealDate.restaurant_picture: date_update.restaurant_picture
        })
        session.commit()

    @staticmethod
    def deleteDate(date_id):
        session.query(MealDate).filter(id == date_id).delete()
        session.commit()
