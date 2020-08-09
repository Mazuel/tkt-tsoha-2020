import messageforum
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from messageforum import routes