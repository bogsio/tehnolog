import logging
from logging.handlers import RotatingFileHandler
from app import app



if __name__ == "__main__":
    handler = RotatingFileHandler('tehnolog.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True)