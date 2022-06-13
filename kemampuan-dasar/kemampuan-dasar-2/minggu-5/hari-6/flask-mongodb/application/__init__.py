from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# TO FIND SECRETS KEY IS
# TO TERMINAL THAT FOLDER ARE  PUT SOURCE VENV/BIN/ACTIVATE
# AND THEN TEXT PYTHON3
# >>> IMPORT SECRETS
# >>> SECRETS.TOKEN_HEX(20)
# THERE ARE SECRET KEY 
app.config["SECRET_KEY"] = "5470ac5f1f71d2b499c126797de88759a59d7e86"
app.config["MONGO_URI"] = "mongodb+srv://oksip:umbara_77@oksiip.rbu8b8f.mongodb.net/?retryWrites=true&w=majority"

# setyp mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes 
