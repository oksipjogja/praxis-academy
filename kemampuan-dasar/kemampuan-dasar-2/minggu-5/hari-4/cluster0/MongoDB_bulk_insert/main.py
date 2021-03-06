from datetime import date
from dotenv import load_dotenv, find_dotenv 
import os
from datetime import datetime as dt
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")


connection_string = f"mongodb+srv://oksipjogja:{password}@cluster0.2bla9.mongodb.net/?retryWrites=true&w=majority&authSource=admin"

client = MongoClient(connection_string)

# DATABASE SEKOLAH
# dbs = client.list_database_names()
# sekolah = client.sekolah

# def create_murid_collection():
#   murid_validator = {
#       "$jsonSchema": {
#         "bsonType": "object",
#         "required": [ "name", "year", "major", "address" ],
#         "properties": {
#             "name": {
#               "bsonType": "string",
#               "description": "must be a string and is required"
#             },
#             "year": {
#               "bsonType": "int",
#               "minimum": 2017,
#               "maximum": 3017,
#               "description": "must be an integer in [ 2017, 3017 ] and is required"
#             },
#             "major": {
#               "enum": [ "Math", "English", "Computer Science", "History", "null" ],
#               "description": "can only be one of the enum values and is required"
#             },
#             "gpa": {
#               "bsonType": [ "double" ],
#               "description": "must be a double if the field exists"
#             },
#             "address": {
#               "bsonType": "object",
#               "required": [ "city" ],
#               "properties": {
#                   "street": {
#                     "bsonType": "string",
#                     "description": "must be a string if the field exists"
#                   },
#                   "city": {
#                     "bsonType": "string",
#                     "description": "must be a string and is required"
#                   }
#               }
#             }
#         }
#       }
#     }

#   try:
#     sekolah.create_collection("murid")
#   except Exception as e:
#     print(e)   

#   sekolah.command("collMod", "murid", validator=murid_validator)

# create_murid_collection()

# def create_guru_collection():     # ---> def (define)
#   guru_validator = {
#     "$jsonSchema": {
#       "bsonType": "object",
#       "required": [ "first_name", "last_name", "mobile_phone", "date_of_birth" ],
#       "properties": {
#           "first_name": {
#             "bsonType": "string",
#             "description": "must be a string and is required"
#           },
#           "last_name": {
#             "bsonType": "string",
#             "description": "must be a string and is required"
#           },
#           "mobile_phone": {
#             "bsonType": "string",
#             "description": "must be a string and is required"
#           },
#           "date_of_birth": {
#             "bsonType": "date",
#             "description": "must be a date and is required"
#           },           
#         }
#       }
#     }
  
#   try:
#     sekolah.create_collection("guru")
#   except Exception as e:
#     print(e)   

#   sekolah.command("collMod", "guru", validator=guru_validator)

# create_guru_collection()
   
# def buat_data():
#   gurus = [
#     {
#       "first_name": "Saridjan",
#       "last_name": "Wongso",
#       "mobile_phone": "0812272262526",
#       "date_of_birth": dt(1971, 8, 20)
#     },
#     {
#       "first_name": "Novie",
#       "last_name": "Andaresta",
#       "mobile_phone": "081327278989",
#       "date_of_birth": dt(1987, 6, 12)
#     },
#     {
#       "first_name": "Berto",
#       "last_name": "Armando",
#       "mobile_phone": "0852676762211",
#       "date_of_birth": dt(1982, 4, 15)
#     },
#     {
#       "first_name": "Wenni",
#       "last_name": "Aldhila",
#       "mobile_phone": "088802239822",
#       "date_of_birth": dt(1983, 5, 23)
#     },
#   ]

#   guru_col = sekolah.guru
#   gurus = guru_col.insert_many(gurus)
  
#   murids = [
#     {
#       "name": "Dani Prasetya", 
#       "year": 2019, 
#       "major": "Math", 
#       "address": {
#         "city": "Surakarta",
#         "street": "Jl. Slamet Riyadi No 12"
#       }
#     },
#      {
#       "name": "Ahmad Bahrowi", 
#       "year": 2018, 
#       "major": "Computer Science", 
#       "address": {
#         "city": "Surakarta",
#         "street": "Jl. Sugeng Jeroni No 5A"
#       }
#     },
#      {
#       "name": "Andra Mahesa", 
#       "year": 2018, 
#       "major": "History", 
#       "address": {
#         "city": "Surakarta",
#         "street": "Jl. Ahmad Yani No 21A"
#       }
#     },
#      {
#       "name": "Nita Dahlian", 
#       "year": 2018, 
#       "major": "English", 
#       "address": {
#         "city": "Surakarta",
#         "street": "Jl. Palur No 234"
#       }
#     },
#   ]
#   murid_col = sekolah.murid
#   murid_col.insert_many(murids)
  
# buat_data() 

# ---------------------------------------------------------------------------------

# DATABASE PENERBIT
dbs = client.list_database_names()
penerbit = client.penerbit

def create_book_collection():
  book_validator = {
      "$jsonSchema": {
          "bsonType": "object",
          "required": [ 
            "title", 
            "authors", 
            "publish_date", 
            "type", 
            "copies" 
            ],
          "properties": {
            "title": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "authors": {
                "bsonType": "array",
                "items": {
                  "bsonType": "objectId",
                  "description": "must be a objectid and is required"
                }              
            },
            "publish_date": {
                "bsonType": "date",
                "description": "must be a date an is required"
            },
            "type": {
                "enum": [ 
                  "Fiction", 
                  "Non-Fiction" 
                  ],
                "description": "can only be one of the enum values and is required"
            },
            "copies": {
                "bsonType": "int",
                "minimum": 0,
                "description": "must be an integer greater than 0 and is required"
            },
          }
      }
  }
                                    
  try:
    penerbit.create_collection("book")
  except Exception as e:
    print(e)   

  penerbit.command("collMod", "book", validator=book_validator)
  
create_book_collection()

def create_author_collection():
  author_validator = {
    "$jsonSchema": {
      "bsonType": "object",
      "required": [ 
        "first_name", 
        "last_name", 
        "date_of_birth"
        ],
      "properties": {
        "first_name": {
            "bsonType": "string",
            "description": "must be a string and is required"
        },
        "last_name": {
            "bsonType": "string",
            "description": "must be a string and is required"
        },              
        "date_of_birth": {
            "bsonType": "date",
            "description": "must be a date an is required"
        },
      }
    }
  }  
  
  try:
    penerbit.create_collection("author")
  except Exception as e:
    print(e)   

  penerbit.command("collMod", "author", validator=author_validator)
create_author_collection()

def create_data():
  authors = [
    {
      "first_name": "Andrew",
      "last_name": "Simson",
      "date_of_birth": dt(1998, 4, 24)
    },
    {
      "first_name": "Marshall",
      "last_name": "Edward",
      "date_of_birth": dt(1994, 3, 14)
    },
    {
      "first_name": "Billy",
      "last_name": "Jackson",
      "date_of_birth": dt(1999, 8, 5)
    },
    {
      "first_name": "Natalie",
      "last_name": "Cardwell",
      "date_of_birth": dt(1997, 10, 2)
    }
  ]
  
  author_col = penerbit.author
  authors = author_col.insert_many(authors).inserted_ids
  
  books = [
    {
      "title": "MongoDB Advance Tutorial", 
      "authors": [authors[1]], 
      "publish_date": dt.today(), 
      "type": "Non-Fiction", 
      "copies": 5 
    },
    {
      "title": "Python For Dummies", 
      "authors": [authors[0]], 
      "publish_date": dt(2000, 1, 17), 
      "type": "Non-Fiction", 
      "copies": 5 
    },
      {
      "title": "Nineteen Eighty_Four", 
      "authors": [authors[1]], 
      "publish_date": dt(1949, 6, 8), 
      "type": "Fiction", 
      "copies": 5 
    },
      {
      "title": "The Great Gatsby", 
      "authors": [authors[3]], 
      "publish_date": dt(2014, 5, 23), 
      "type": "Fiction", 
      "copies": 5 
    },
        {
      "title": "Moby Dick", 
      "authors": [authors[2]], 
      "publish_date": dt(1851, 9, 24), 
      "type": "Fiction", 
      "copies": 5 
    },
  ]
  
  book_col = penerbit.book
  book_col.insert_many(books)
  
create_data()









