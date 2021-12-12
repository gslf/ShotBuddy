from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yqb8ak-Kvijaod82jaDsGjkobhjpx8(usnv!jabjdbaonzpejubsreh/++-abkajs'

from webapp import routes