from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Request, Proposal, MealDate


class DatabaseService:
    def __init__(self):
        engine = create_engine('sqlite:///meetneat.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def getUsers(self):
        return self.session.query(User).all()

    def getUser(self, user_id):
        return self.session.query(User).filter_by(id=user_id).one()

    def addUser(self, user):
        self.session.add(user)
        self.session.commit()

    def updateUser(self, user_id, user_update):
        self.session.query(User).filter(id == user_id).update({
            User.email: user_update.email,
            User.email: user_update.picture
        })
        self.session.commit()

    def deleteUser(self, user_id):
        self.session.query(User).filter(id == user_id).delete()
        self.session.commit()

    def getRequests(self):
        return self.session.query(Request).all()

    def getRequest(self, request_id):
        return self.session.query(Request).filter_by(id=request_id).one()

    def addRequest(self, request):
        self.session.add(request);
        self.session.commit()

    def updateRequest(self, request_id, request_update):
        self.session.query(Request).filter(id == request_id).update({
            Request.meal_type: request_update.meal_type,
            Request.location_string: request_update.location_string,
            Request.latitude: request_update.latitude,
            Request.longitude: request_update.longitude,
            Request.meal_time: request_update.meal_time,
            Request.filled: request_update.filled
        })
        self.session.commit()

    def deleteRequest(self, request_id):
        self.session.query(Request).filter(id == request_id).delete()
        self.session.commit()

    def getProposals(self):
        return self.session.query(Proposal).all()

    def getProposal(self, proposal_id):
        return self.session.query(Proposal).filter_by(id=proposal_id).one()

    def addProposal(self, proposal):
        self.session.add(proposal)
        self.session.commit()

    def updateProposal(self, proposal_id, proposal_update):
        self.session.query(Proposal).filter(id == proposal_id).update({
            Proposal.user_proposed_to: proposal_update.user_proposed_to,
            Proposal.user_proposed_from: proposal_update.user_proposed_from,
            Proposal.request_id: proposal_update.request_id,
            Proposal.filled: proposal_update.filled
        })
        self.session.commit()

    def deleteProposal(self, proposal_id):
        self.session.query(Request).filter(id == proposal_id).delete()
        self.session.commit()

    def getDates(self):
        return self.session.query(MealDate).all()

    def getDate(self, date_id):
        return self.session.query(MealDate).filter_by(id=date_id).one()

    def addDate(self, date):
        self.session.add(date)
        self.session.commit()

    def updateDate(self, date_id, date_update):
        self.session.query(MealDate).filter(id == date_id).update({
            MealDate.user_1: date_update.user_1,
            MealDate.user_2: date_update.user_2,
            MealDate.restaurant_name: date_update.restaurant_update,
            MealDate.restaurant_address: date_update.restaurant_address,
            MealDate.restaurant_picture: date_update.restaurant_picture
        })
        self.session.commit()

    def deleteDate(self, date_id):
        self.session.query(MealDate).filter(id == date_id).delete()
        self.session.commit()
