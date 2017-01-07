import logging
from logging.handlers import RotatingFileHandler

from app import create_app

app = create_app()

if __name__ == '__main__':
    handler = RotatingFileHandler('meetneat.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(app.config['LOGGING_FORMAT']))
    app.logger.addHandler(handler)

    app.debug = True
    app.run(host=app.config['HOST'], port=app.config['PORT'])
