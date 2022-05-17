from dotenv import load_dotenv, find_dotenv 
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")


connection_string = f"mongodb+srv://oksipjogja:{password}@cluster0.2bla9.mongodb.net/?rmongodb+srv://oksipjogja:<password>@cluster0.2bla9.mongodb.net/?retryWrites=true&w=majorityetryWrites=true&w=majority"

client = MongoClient(connection_string)
