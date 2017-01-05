import os

from flask import Flask
from sqlalchemy import create_engine

from app.v1.utils.database_provider import Base
from app.v1.v1 import api_v1_bp, API_VERSION_V1


def create_app(environment=None):
    app = Flask(__name__)

    engine = create_engine('sqlite:///meetneat.db')
    Base.metadata.create_all(engine)

    if not environment:
        environment = os.environ.get('FLASK_CONFIG', 'development')

    app.config.from_object('config.{}'.format(environment.capitalize()))
    app.config.from_pyfile(
        'config_{}.py'.format(environment.lower()),
        silent=True
    )

    app.register_blueprint(
        api_v1_bp,
        url_prefix='{prefix}/v{version}'.format(
            prefix=app.config['URL_PREFIX'],
            version=API_VERSION_V1))

    return app
