from bson import ObjectId
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
# fungsi insertOne
#   collection = perpustakaan_db.katalog
#   app_document = {
#     "Judul" : "Wanda Hamidah Lagi Ngoding",
#     "Penerbit" : "Syafak Publish"
#   }
#   inserted_id = collection.insert_one(app_document).inserted_id
  
# insert_app_doc()

pabrik = client.pabrik
karyawan_col = pabrik.karyawan
# def buat_document():

# # fungsi insertMany
#   first_names = ["Dela", "Suwarno", "Wagiman", "Subagyo", "Parjiman", "Hendi"]
#   last_names = ["Suwarni", "Hadiprawiro", "Harjolukito", "Makarti", "Suryodiningrat", "Oktavianus"]
#   ages = [35, 40, 32, 33, 30, 25]
  
#   docs = []

#   for first_name, last_name, age in zip(first_names, last_names, ages):
#     doc = {"first_name" : first_name, "last_name" : last_name, "age" : age}
#     docs.append(doc)
    
#   karyawan_col.insert_many(docs)
  
# buat_document()


### Fungsi find_all
printer = pprint.PrettyPrinter()

# METHOD DEF FIND_ALL_n()
   #  CARA 1 : FIND ALL
# def find_all_orang():
#   orang = karyawan_col.find()
#   # print(list(orang))
  
#   for karyawan in orang:
#     printer.pprint(karyawan)
    
# find_all_orang()
  
  # CARA 2 : FIND__id
# def find__id():
#   _id = karyawan_col.find_one({ "_id" : ObjectId("6285d3eb8e7d281c4f7528ea") })
#   printer.pprint(_id)
  
# find__id()

#   # CARA 3 : FIND_NAME
# def find_dela():
#   dela = karyawan_col.find_one({"first_name":"Dela"})
#   printer.pprint(dela)
  
# find_dela()

# def count_all_orang():
#   count = karyawan_col.count_documents(filter={})
#   print("Jumlah karyawan : ", count)
  
# count_all_orang()


