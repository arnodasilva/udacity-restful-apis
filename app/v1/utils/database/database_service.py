from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from app.v1.dates.models import Date
from app.v1.proposals.models import Proposal
from app.v1.requests.models import Request
from app.v1.users.models import User
from app.v1.utils.database.database_provider import Base
from app.v1.utils.errors.web_application_exception import WebApplicationException

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
        try:
            return session.query(User).filter_by(id=user_id).one()
        except NoResultFound as e:
            current_app.logger.error(e.message)
            raise WebApplicationException('Resource not found',
                                          'The user resource with the id %d does not exist' % user_id,
                                          status_code=404)

    @staticmethod
    def addUser(user):
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        except (TypeError, IntegrityError)as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Validation error.',
                                          'A validation constraint has not been respected',
                                          status_code=400)

    @staticmethod
    def updateUser(user_id, user_update):
        try:
            if DatabaseService.getUser(user_id):
                session.query(User).filter_by(id=user_id).update(dict(user_update))
                session.commit()
                return DatabaseService.getUser(user_id)
        except (TypeError, IntegrityError)as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Validation error.',
                                          'A validation constraint has not been respected',
                                          status_code=400)

    @staticmethod
    def deleteUser(user_id):
        try:
            if DatabaseService.getUser(user_id):
                session.query(User).filter_by(id=user_id).delete()
                session.commit()
        except (TypeError, IntegrityError)as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Internal Server Error',
                                          'If the problem persists, please contact the developer for assistance',
                                          status_code=500)

    @staticmethod
    def getRequests():
        return session.query(Request).all()

    @staticmethod
    def getRequest(request_id):
        try:
            return session.query(Request).filter_by(id=request_id).one()
        except NoResultFound as e:
            current_app.logger.error(e.message)
            raise WebApplicationException('Resource not found',
                                          'The request resource with the id %d does not exist' % request_id,
                                          status_code=404)

    @staticmethod
    def addRequest(request):
        try:
            if DatabaseService.getUser(request.user_id):
                session.add(request)
                session.commit()
                session.refresh(request)
                return request
        except (TypeError, IntegrityError) as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Internal Server Error',
                                          'If the problem persists, please contact the developer for assistance',
                                          status_code=500)

    @staticmethod
    def updateRequest(request_id, request_update):
        try:
            if DatabaseService.getRequest(request_id) \
                    and DatabaseService.getUser(request_update.user_id):
                session.query(Request).filter_by(id=request_id).update(dict(request_update))
                session.commit()
                return DatabaseService.getRequest(request_id)
        except (TypeError, IntegrityError) as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Internal Server Error',
                                          'If the problem persists, please contact the developer for assistance',
                                          status_code=500)

    @staticmethod
    def deleteRequest(request_id):
        try:
            if DatabaseService.getRequest(request_id):
                session.query(Request).filter_by(id=request_id).delete()
                session.commit()
        except (TypeError, IntegrityError) as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Internal Server Error',
                                          'If the problem persists, please contact the developer for assistance',
                                          status_code=500)

    @staticmethod
    def getProposals():
        return session.query(Proposal).all()

    @staticmethod
    def getProposal(proposal_id):
        try:
            return session.query(Proposal).filter_by(id=proposal_id).one()
        except NoResultFound as e:
            current_app.logger.error(e.message)
            raise WebApplicationException('Resource not found',
                                          'The proposal resource with the id %d does not exist' % proposal_id,
                                          status_code=404)

    @staticmethod
    def addProposal(proposal):
        try:
            if DatabaseService.getRequest(proposal.request_id) \
                    and DatabaseService.getUser(proposal.user_proposed_to) \
                    and DatabaseService.getUser(proposal.user_proposed_from):
                session.add(proposal)
                session.commit()
                session.refresh(proposal)
                return proposal
        except (TypeError, IntegrityError) as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Internal Server Error',
                                          'If the problem persists, please contact the developer for assistance',
                                          status_code=500)

    @staticmethod
    def updateProposal(proposal_id, proposal_update):
        try:
            if DatabaseService.getProposal(proposal_id) \
                    and DatabaseService.getRequest(proposal_update.request_id) \
                    and DatabaseService.getUser(proposal_update.user_proposed_to) \
                    and DatabaseService.getUser(proposal_update.user_proposed_from):
                session.query(Proposal).filter_by(id=proposal_id).update(dict(proposal_update))
                session.commit()
        except (TypeError, IntegrityError) as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Internal Server Error',
                                          'If the problem persists, please contact the developer for assistance',
                                          status_code=500)

    @staticmethod
    def deleteProposal(proposal_id):
        try:
            if DatabaseService.getProposal(proposal_id):
                session.query(Request).filter_by(id=proposal_id).delete()
                session.commit()
        except (TypeError, IntegrityError) as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Internal Server Error',
                                          'If the problem persists, please contact the developer for assistance',
                                          status_code=500)

    @staticmethod
    def getDates():
        return session.query(Date).all()

    @staticmethod
    def getDate(date_id):
        try:
            return session.query(Date).filter_by(id=date_id).one()
        except NoResultFound as e:
            current_app.logger.error(e.message)
            raise WebApplicationException('Resource not found',
                                          'The mealdate resource with the id %d does not exist' % date_id,
                                          status_code=404)

    @staticmethod
    def addDate(date):
        try:
            if DatabaseService.getUser(date.user_1) \
                    and DatabaseService.getUser(date.user_2):
                session.add(date)
                session.commit()
                session.refresh(date)
                return date
        except (TypeError, IntegrityError) as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Internal Server Error',
                                          'If the problem persists, please contact the developer for assistance',
                                          status_code=500)

    @staticmethod
    def updateDate(date_id, date_update):
        try:
            if DatabaseService.getDate(date_id) \
                    and DatabaseService.getUser(date_update.user_1) \
                    and DatabaseService.getUser(date_update.user_2):
                session.query(Date).filter_by(id=date_id).update(dict(date_update))
                session.commit()
        except (TypeError, IntegrityError) as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Internal Server Error',
                                          'If the problem persists, please contact the developer for assistance',
                                          status_code=500)

    @staticmethod
    def deleteDate(date_id):
        try:
            if DatabaseService.getDate(date_id):
                session.query(Date).filter_by(id=date_id).delete()
                session.commit()
        except (TypeError, IntegrityError) as e:
            session.rollback()
            current_app.logger.error(e.message)
            raise WebApplicationException('Internal Server Error',
                                          'If the problem persists, please contact the developer for assistance',
                                          status_code=500)
