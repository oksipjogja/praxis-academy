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

# melakukan input data denganfungsi insertMany
# def buat_document():
#   first_names = ["Dela", "Suwarno", "Wagiman", "Subagyo", "Parjiman", "Hendi"]
#   last_names = ["Suwarni", "Hadiprawiro", "Harjolukito", "Makarti", "Suryodiningrat", "Oktavianus"]
#   ages = [35, 40, 32, 33, 30, 25]
  
#   docs = []

#   for first_name, last_name, age in zip(first_names, last_names, ages):
#     doc = {"first_name" : first_name, "last_name" : last_name, "age" : age}
#     docs.append(doc)
#   karyawan_col.insert_many(docs)
  
# buat_document()

# Fungsi find_all
printer = pprint.PrettyPrinter()

# METHOD DEF FIND_ALL_n()
   #  CARA 1 : FIND ALL
# def find_all_orang():
#   orang = karyawan_col.find()
#   # print(list(orang))
  
#   for karyawan in orang:
#     printer.pprint(karyawan)
    
# find_all_orang()
# ---> {'_id': ObjectId('6286a871cedb34fcf2215aab'),
      #  'age': 32,
      #  'first_name': 'Wagiman',
      #  'last_name': 'Harjolukito'}
      # donie@donie-ThinkPad-T430:~/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/minggu-5/hari-4/cluster0/CRUD$ /bin/python3 /home/donie/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/minggu-5/hari-4/cluster0/CRUD/main.py
      # {'_id': ObjectId('6286a871cedb34fcf2215aa9'),
      #  'age': 35,
      #  'first_name': 'Dela',
      #  'last_name': 'Suwarni'}
      # {'_id': ObjectId('6286a871cedb34fcf2215aaa'),
      #  'age': 40,
      #  'first_name': 'Suwarno',
      #  'last_name': 'Hadiprawiro'}
      # {'_id': ObjectId('6286a871cedb34fcf2215aab'),
      #  'age': 32,
      #  'first_name': 'Wagiman',
      #  'last_name': 'Harjolukito'}
      # {'_id': ObjectId('6286a871cedb34fcf2215aac'),
      #  'age': 33,
      #  'first_name': 'Subagyo',
      #  'last_name': 'Makarti'}
      # {'_id': ObjectId('6286a871cedb34fcf2215aad'),
      #  'age': 30,
      #  'first_name': 'Parjiman',
      #  'last_name': 'Suryodiningrat'}
      # {'_id': ObjectId('6286a871cedb34fcf2215aae'),
      #  'age': 25,
      #  'first_name': 'Hendi',
      #  'last_name': 'Oktavianus'}
  
  # CARA 2 : FIND__id
# def find__id():
#   _id = karyawan_col.find_one({ "_id" : ObjectId("6286a871cedb34fcf2215aab") })
#   printer.pprint(_id)
  
# find__id()
# ---> {'_id': ObjectId('6286a871cedb34fcf2215aab'),
#      'age': 32,
#      'first_name': 'Wagiman',
#      'last_name': 'Harjolukito'}

#   # CARA 3 : FIND_NAME
# def find_dela():
#   dela = karyawan_col.find_one({"first_name":"Dela"})
#   printer.pprint(dela)
  
# find_dela()
# # ---> {'_id': ObjectId('6286a871cedb34fcf2215aa9'),
#        'age': 35,
#        'first_name': 'Dela',
#        'last_name': 'Suwarni'}

# def count_all_orang():
#   count = karyawan_col.count_documents(filter={})
#   print("Jumlah karyawan : ", count)
  
# count_all_orang()
# --> Jumlah karyawan :  6                                                                                             SEJATI RENTAL                                                                                   PURWOKERTO


# def cari_orang_by_id(karyawan_id):
#   from bson.objectid import ObjectId
  
#   _id = ObjectId(karyawan_id)
#   karyawan = karyawan_col.find_one({"_id": _id})
#   printer.pprint(karyawan)
  
# cari_orang_by_id("6285d3eb8e7d281c4f7528ea")
    
# def cari_usia_range(min_age, max_age):
#   query = {"$and" :  [
#       {"age" : {"$gte" : min_age}},
#       {"age" : {"$lte" : max_age}}
#     ]}
  
#   orang = karyawan_col.find(query).sort("age")
#   for karyawan in orang:
#     printer.pprint(karyawan)
    
# cari_usia_range(30, 42)

# def project_kolom():
#   kolom = {"_id" : 0, "first_name" : 1, "last_name" : 1}
#   orang = karyawan_col.find({}, kolom)
#   for karyawan in orang:
#     printer.pprint(karyawan)
  
# project_kolom()
# ---> {'first_name': 'Dela', 'last_name': 'Suwarni'}
      # {'first_name': 'Suwarno', 'last_name': 'Hadiprawiro'}
      # {'first_name': 'Wagiman', 'last_name': 'Harjolukito'}
      # {'first_name': 'Subagyo', 'last_name': 'Makarti'}
      # {'first_name': 'Parjiman', 'last_name': 'Suryodiningrat'}
      # {'first_name': 'Hendi', 'last_name': 'Oktavianus'}

#  UPDATAE DOCUMENT
# def update_person_by_id(karyawan_id):
#   from bson.objectid import ObjectId
  
#   _id = ObjectId(karyawan_id)
  
#   all_update = {
#     "$set": {"new_field": True},
#     "$inc": {"age": 1},      # ---> $inc = increment/kenaikan
#     "$rename": {"first_name": "first", "last_name": "last"}
#   }
#   karyawan_col.update_one({"_id": _id}, all_update)
# update_person_by_id("6286a871cedb34fcf2215aad")
# ===>
# _id: ObjectId('6286a871cedb34fcf2215aad')  --> _id: ObjectId('6286a871cedb34fcf2215aad')    
# first_name: "Parjiman"                     --> first: "Parjiman"
# last_name: "Suryodiningrat"                --> last: "Suryodiningrat"
# age: 30                                    --> age: 31

# def update_person_by_id(karyawan_id):
#   from bson.objectid import ObjectId
  
#   _id = ObjectId(karyawan_id)
#   karyawan_col.update_one({"_id": _id}, {"$unset": {"new_field": ""}}) # ---> mengembalikan ke semula
# update_person_by_id("6286a871cedb34fcf2215aad")
# ===> kembali seperti semula

# def replace_one(karyawan_id):
#   from bson.objectid import ObjectId
#   _id = ObjectId(karyawan_id)
  
#   new_doc = {
#     "first_name" : "new first name",
#     "last_name" : "new last name",
#     "age" : 100
#   }
#   karyawan_col.replace_one({"_id": _id}, new_doc)
  
# replace_one("6286a871cedb34fcf2215aad")
# ===>
# _id: ObjectId('6286a871cedb34fcf2215aad')   ----  _id: ObjectId('6286a871cedb34fcf2215aad')
# first_name: "Parjiman"                      ----  first_name: "new first name"
# last_name: "Suryodiningrat"                 ----  last_name: "new last name" 
# age: 30                                     ----  age: 100

# def delete_doc_by_id(karyawan_id):
#   from bson.objectid import ObjectId
#   _id = ObjectId(karyawan_id)
#   karyawan_col.delete_one({"_id": _id})
  
# delete_doc_by_id("6286a871cedb34fcf2215aad")
# ---> delete success _id : "6286a871cedb34fcf2215aad" its doesn't exist anymore

# ---------------Menambah Data Array -------------------------------------
alamat = {
  "_id": "6286a871cedb34fcf2215aad",
  "jalan": "Jalak Raya",
  "nomer": 15,
  "kota": "Magetan",
  "negara": "Indonesia",
  "kode_pos": "52165"
}
# METODE 1
# def tambah_alamat_embed(karyawan_id, alamat):
#   from bson.objectid import ObjectId
#   _id = ObjectId(karyawan_id)
  
#   karyawan_col.update_one(
#     {"_id" : _id}, {"$addToSet": {"almt": alamat}})

# tambah_alamat_embed("6286a871cedb34fcf2215aab", alamat)
# ===>
# _id: ('6286a871cedb34fcf2215aab')
# first_name: "Wagiman"
# last_name: "Harjolukito"
# age: 32
# alamatss: Array
# 0
# Object
# _id: "6286a871cedb34fcf2215aad"
# jalan: "Kalamandu Raya"
# nomer: 25
# kota:"Madiun"
# negara: "Indonesia"
# kode_pos: "55265"

# METODE 2
# def tambah_alamat_relationship(karyawan_id, alamat):
#   from bson.objectid import ObjectId
#   _id = ObjectId(karyawan_id)
  
#   alamat = alamat.copy()
#   alamat["owner_id"] = karyawan_id
  
#   alamat_col = pabrik.alamat
#   alamat_col.insert_one(alamat)

# tambah_alamat_relationship("6286a871cedb34fcf2215aaa", alamat)
# ===> ada collection baru root dibawah collection dbs
# _id: ("6286a871cedb34fcf2215aad")
# jalan: "Jalak Raya"
# nomer: 15
# kota: "Magetan"
# negara: "Indonesia"
# kode_pos: "52165"
# owner_id: "6286a871cedb34fcf2215aaa"




