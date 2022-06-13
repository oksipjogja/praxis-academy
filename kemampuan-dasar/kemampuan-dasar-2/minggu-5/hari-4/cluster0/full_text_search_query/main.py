from datetime import date
from dotenv import load_dotenv, find_dotenv 
import os
from datetime import datetime as dt
import json
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())
printer = pprint.PrettyPrinter()
from pprint import PrettyPrinter

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://oksipjogja:{password}@cluster0.2bla9.mongodb.net/?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(connection_string)

jeoprady_db = client.jeoprady_db
question = jeoprady_db.question