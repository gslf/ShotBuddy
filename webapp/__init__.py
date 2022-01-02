from flask import Flask
from flask_login import LoginManager

import logging.config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yqb8ak-Kvijaod82jaDsGjkobhjpx8(usnv!jabjdbaonzpejubsreh/++-abkajs'

login = LoginManager(app)

# Log setup
logging.config.fileConfig("log_config.ini", disable_existing_loggers=False)


from webapp import routes