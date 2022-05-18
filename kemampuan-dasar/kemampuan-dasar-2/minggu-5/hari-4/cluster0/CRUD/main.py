from dotenv import load_dotenv, find_dotenv
import os
import pprint
from matplotlib import collections
from pymongo import MongoClient

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://oksipjogja:{password}@cluster0.2bla9.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

dbs = client.list_database_names()
toko_besi_db = client.toko_besi
# print(dbs)  --> ['toko_besi', 'admin', 'local']


# col = toko_besi_db.list_collection_names()
# print(col) outputnya -> ["'gudang'"]

  """RELATIONAL DATA BASE MANAGEMENT SYSTEMS
        SQL (STRUCTURED QUERY LANGUAGE)
  """
  
  
  