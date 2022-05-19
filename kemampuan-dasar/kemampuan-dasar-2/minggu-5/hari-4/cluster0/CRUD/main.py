from dotenv import load_dotenv, find_dotenv
import os
import pprint

from pymongo import MongoClient

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://oksipjogja:{password}@cluster0.2bla9.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

# dbs = client.list_database_names()
# perpustakaan_db = client.perpustakaan
# print(dbs)  --> ['toko_besi', 'admin', 'local']


# col = toko_besi_db.list_collection_names()
# print(col) outputnya -> ["'gudang'"]

# def insert_app_doc():clear

#   collection = perpustakaan_db.katalog
#   app_document = {
#     "Judul" : "Wanda Hamidah Lagi Ngoding",
#     "Penerbit" : "Syafak Publish"
#   }
#   inserted_id = collection.insert_one(app_document).inserted_id
  
# insert_app_doc()

pabrik = client.pabrik
karyawan_col = pabrik.karyawan

def buat_document():
  first_names = ["Dela", "Suwarno", "Wagiman", "Subagyo", "Parjiman", "Hendi"]
  last_names = ["Suwarni", "Hadiprawiro", "Harjolukito", "Makarti", "Suryodiningrat", "Oktavianus"]
  ages = [35, 40, 32, 33, 30, 25]
  
  docs = []

  for first_name, last_name, age in zip(first_names, last_names, ages):
    doc = {"first_name" : first_name, "last_name" : last_name, "age" : age}
    docs.append(doc)
    
  karyawan_col.insert_many(docs)
  
buat_document()

printer = pprint.PrettyPrinter()

def find_all_orang():
  orang = karyawan_col.find()
  print(list(orang))
  
  for karyawan in orang:
    printer.pprint(karyawan)
    
find_all_orang()
  
