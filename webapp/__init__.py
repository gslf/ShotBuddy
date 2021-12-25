from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yqb8ak-Kvijaod82jaDsGjkobhjpx8(usnv!jabjdbaonzpejubsreh/++-abkajs'

login = LoginManager(app)

from webapp import routes