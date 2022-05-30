from flask import Flask
from flask_pymongo import PyMongo
import dns


app = Flask(__name__)
app.config["SECRET_KEY"] = "e1134d0dd7e60e81832238bfa5c9744be4292422"
app.config['MONGO_URI'] = "mongodb+srv://oksip:umbara_77@oksiip.rbu8b8f.mongodb.net/?retryWrites=true&w=majority"

# setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes