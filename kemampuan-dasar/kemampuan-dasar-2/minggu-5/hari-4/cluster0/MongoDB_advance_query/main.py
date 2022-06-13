from datetime import date
from dotenv import load_dotenv, find_dotenv 
import os
from datetime import datetime as dt
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())
printer = pprint.PrettyPrinter()

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
      "date_of_birth": dt(2000, 4, 24)
    },
    {
      "first_name": "Marshall",
      "last_name": "Edward",
      "date_of_birth": dt(1903, 3, 14)
    },
    {
      "first_name": "Billy",
      "last_name": "Jackson",
      "date_of_birth": dt(1819, 8, 5)
    },
    {
      "first_name": "Natalie",
      "last_name": "Cardwell",
      "date_of_birth": dt(1896, 10, 2)
    }
  ]
  
  author_col = penerbit.author
  authors = author_col.insert_many(authors).inserted_ids
  
  # books = [
  #   {
  #     "title": "MongoDB Advance Tutorial", 
  #     "authors": [authors[1]], 
  #     "publish_date": dt.today(), 
  #     "type": "Non-Fiction", 
  #     "copies": 5 
  #   },
  #   {
  #     "title": "Python For Dummies", 
  #     "authors": [authors[0]], 
  #     "publish_date": dt(2000, 1, 17), 
  #     "type": "Non-Fiction", 
  #     "copies": 5 
  #   },
  #     {
  #     "title": "Nineteen Eighty_Four", 
  #     "authors": [authors[2]], 
  #     "publish_date": dt(1949, 6, 8), 
  #     "type": "Fiction", 
  #     "copies": 5 
  #   },
  #     {
  #     "title": "The Great Gatsby", 
  #     "authors": [authors[3]], 
  #     "publish_date": dt(2014, 5, 23), 
  #     "type": "Fiction", 
  #     "copies": 5 
  #   },
  #       {
  #     "title": "Moby Dick", 
  #     "authors": [authors[2]], 
  #     "publish_date": dt(1851, 9, 24), 
  #     "type": "Fiction", 
  #     "copies": 5 
  #   },
  # ]
  
  # book_col = penerbit.book
  # book_col.insert_many(books)
  
# create_data()

# books_containing_a = penerbit.book.find({"title": {"$regex": "a{1}"}})  # --->$regex (regular expression)
# printer.pprint(list(books_containing_a))
# -----------------------------------------------------------------------
# collection book already exists
# collection author already exists
# [{'_id': ObjectId('6289ed8628db7b4d41d9a4b8'),
#   'authors': [ObjectId('6289ed8628db7b4d41d9a4b5')],
#   'copies': 5,
#   'publish_date': datetime.datetime(2022, 5, 22, 15, 0, 6, 704000),
#   'title': 'MongoDB Advance Tutorial',
#   'type': 'Non-Fiction'},
#  {'_id': ObjectId('6289ed8628db7b4d41d9a4bb'),
#   'authors': [ObjectId('6289ed8628db7b4d41d9a4b7')],
#   'copies': 5,
#   'publish_date': datetime.datetime(2014, 5, 23, 0, 0),
#   'title': 'The Great Gatsby',
#   'type': 'Fiction'}]
# -------------------------------------------------------------------
# books_containing_b = penerbit.book.find({"title": {"$regex": "b{1}"}})  # --->$regex (regular expression)
# printer.pprint(list(books_containing_b))
# --------------------------------------------------------------------
# [{'_id': ObjectId('6289ed8628db7b4d41d9a4bb'),
#   'authors': [ObjectId('6289ed8628db7b4d41d9a4b7')],
#   'copies': 5,
#   'publish_date': datetime.datetime(2014, 5, 23, 0, 0),
#   'title': 'The Great Gatsby',
#   'type': 'Fiction'},
#  {'_id': ObjectId('6289ed8628db7b4d41d9a4bc'),
#   'authors': [ObjectId('6289ed8628db7b4d41d9a4b6')],
#   'copies': 5,
#   'publish_date': datetime.datetime(1851, 9, 24, 0, 0),
#   'title': 'Moby Dick',
#   'type': 'Fiction'}]
# --------------------------------------------------------------------
# books_containing_P = penerbit.book.find({"title": {"$regex": "P{1}"}})  # --->$regex (regular expression)
# printer.pprint(list(books_containing_P))
# --------------------------------------------------------------------
# [{'_id': ObjectId('6289ed8628db7b4d41d9a4b9'),
#   'authors': [ObjectId('6289ed8628db7b4d41d9a4b4')],
#   'copies': 5,
#   'publish_date': datetime.datetime(2000, 1, 17, 0, 0),
#   'title': 'Python For Dummies',
#   'type': 'Non-Fiction'}]
# --------------------------------------------------------------------

# authors_and_books = penerbit.author.aggregate([{
#   "$lookup": {
#     "from" : "book",
#     "localField": "_id",
#     "foreignField": "authors",
#     "as": "books"
#   }
# }])
# printer.pprint(list(authors_and_books))
# --------------------------------------------------------------------
# [{'_id': ObjectId('6289ed8628db7b4d41d9a4b4'),
#   'books': [{'_id': ObjectId('6289ed8628db7b4d41d9a4b9'),
#              'authors': [ObjectId('6289ed8628db7b4d41d9a4b4')],
#              'copies': 5,
#              'publish_date': datetime.datetime(2000, 1, 17, 0, 0),
#              'title': 'Python For Dummies',
#              'type': 'Non-Fiction'}],
#   'date_of_birth': datetime.datetime(1998, 4, 24, 0, 0),
#   'first_name': 'Andrew',
#   'last_name': 'Simson'},
#  {'_id': ObjectId('6289ed8628db7b4d41d9a4b5'),
#   'books': [{'_id': ObjectId('6289ed8628db7b4d41d9a4b8'),
#              'authors': [ObjectId('6289ed8628db7b4d41d9a4b5')],
#              'copies': 5,
#              'publish_date': datetime.datetime(2022, 5, 22, 15, 0, 6, 704000),
#              'title': 'MongoDB Advance Tutorial',
#              'type': 'Non-Fiction'},
#             {'_id': ObjectId('6289ed8628db7b4d41d9a4ba'),
#              'authors': [ObjectId('6289ed8628db7b4d41d9a4b5')],
#              'copies': 5,
#              'publish_date': datetime.datetime(1949, 6, 8, 0, 0),
#              'title': 'Nineteen Eighty_Four',
#              'type': 'Fiction'}],
#   'date_of_birth': datetime.datetime(1994, 3, 14, 0, 0),
#   'first_name': 'Marshall',
#   'last_name': 'Edward'},
#  {'_id': ObjectId('6289ed8628db7b4d41d9a4b6'),
#   'books': [{'_id': ObjectId('6289ed8628db7b4d41d9a4bc'),
#              'authors': [ObjectId('6289ed8628db7b4d41d9a4b6')],
#              'copies': 5,
#              'publish_date': datetime.datetime(1851, 9, 24, 0, 0),
#              'title': 'Moby Dick',
#              'type': 'Fiction'}],
#   'date_of_birth': datetime.datetime(1999, 8, 5, 0, 0),
#   'first_name': 'Billy',
#   'last_name': 'Jackson'},
#  {'_id': ObjectId('6289ed8628db7b4d41d9a4b7'),
#   'books': [{'_id': ObjectId('6289ed8628db7b4d41d9a4bb'),
#              'authors': [ObjectId('6289ed8628db7b4d41d9a4b7')],
#              'copies': 5,
#              'publish_date': datetime.datetime(2014, 5, 23, 0, 0),
#              'title': 'The Great Gatsby'
#              'type': 'Fiction'}],
#   'date_of_birth': datetime.datetime(1997, 10, 2, 0, 0),
#   'first_name': 'Natalie',
#   'last_name': 'Cardwell'}]
# --------------------------------------------------------------------
# authors_book_count = penerbit.author.aggregate([
#   {
#   "$lookup": {
#     "from" : "book",
#     "localField": "_id",
#     "foreignField": "authors",
#     "as": "books"
#     }
#   },
#   {
#     "$addFields": {
#       "total_books": {"$size": "$books"}
#     }
#   },
#   {
#     "$project": {"first_name": 1, "last_name": 1, "total_books": 1, "_id": 0 }
#   }
# ])
# printer.pprint(list(authors_book_count))
# -----------------------------------------------------------------------------
# [{'first_name': 'Andrew', 'last_name': 'Simson', 'total_books': 1},
#  {'first_name': 'Marshall', 'last_name': 'Edward', 'total_books': 2},
#  {'first_name': 'Billy', 'last_name': 'Jackson', 'total_books': 1},
#  {'first_name': 'Natalie', 'last_name': 'Cardwell', 'total_books': 1}]
# -----------------------------------------------------------------------------
# books_with_old_authors = penerbit.book.aggregate([
#   {
#     "$lookup": {
#       "from": "author",
#       "localField": "authors",
#       "foreignField": "_id",
#       "as": "authors"
#     }
#   },
#   {
#     "$set": {
#       "authors": {
#         "$map": {
#           "input": "$authors",
#           "in": {
#             "age": {
#               "$dateDiff": {
#                 "startDate": "$$this.date_of_birth",
#                 "endDate": "$$NOW",
#                 "unit": "year"
#               }
#             },
#             "first_name": "$$this.first_name",
#             "last_name": "$$this.last_name",
#           }
#         }
#       }
#     }
#   },
#   {
#     "$match": {
#       "$and": [
#         {"authors.age": {"$gte": 51}},
#         {"authors.age": {"$lte": 151}},
#       ]
#     }
#   },
#   {
#     "$sort": {
#       "age": 1
#     }
#   }
# ])
# printer.pprint(list(books_with_old_authors))
# ---------------------- PYMONGO ARROW DEMO ----------------------------
# python3 -m pip install jupyter pymongoarrow "pymongo[srv]" pandas numpy
import pyarrow 
from pymongoarrow.api import Schema
from pymongoarrow.monkey import patch_all
import pymongoarrow as pma 
from bson import ObjectId

patch_all() 

author = Schema({"_id": ObjectId, "first_name": pyarrow.string(), "last_name":pyarrow.string(), "date_of_birth": dt})

df = penerbit.author.find_pandas_all({}, schema=author)
print(df.head())
# -----------------------------------------------------------------------
# _id first_name last_name date_of_birth
# 0  b'b\x8ajP<\xbcc\xe0d\x1a\x9a\\'     Andrew    Simson    2000-04-24
# 1   b'b\x8ajP<\xbcc\xe0d\x1a\x9a]'   Marshall    Edward    1903-03-14
# 2   b'b\x8ajP<\xbcc\xe0d\x1a\x9a^'      Billy   Jackson    1819-08-05
# 3   b'b\x8ajP<\xbcc\xe0d\x1a\x9a_'    Natalie  Cardwell    1896-10-02
# -----------------------------------------------------------------------
# arrow_table = penerbit.author.find_arrow_all({}, schema=author)
# print(arrow_table)
# -----------------------------------------------------------------------
# pyarrow.Table
# _id: fixed_size_binary[12]
# first_name: string
# last_name: string
# date_of_birth: timestamp[ms]
# ----
# _id: [[628A6A503CBC63E0641A9A5C,628A6A503CBC63E0641A9A5D,628A6A503CBC63E0641A9A5E,628A6A503CBC63E0641A9A5F]]
# first_name: [["Andrew","Marshall","Billy","Natalie"]]
# last_name: [["Simson","Edward","Jackson","Cardwell"]]
# date_of_birth: [[2000-04-24 00:00:00.000,1903-03-14 00:00:00.000,1819-08-05 00:00:00.000,1896-10-02 00:00:00.000]]
# -----------------------------------------------------------------------
darrays = penerbit.author.find_numpy_all({}, schema=author)
print(darrays)
# -------------------------------------------------------------------------------------------------------------------------
#                               _id first_name last_name date_of_birth
# 0  b'b\x8ajP<\xbcc\xe0d\x1a\x9a\\'     Andrew    Simson    2000-04-24
# 1   b'b\x8ajP<\xbcc\xe0d\x1a\x9a]'   Marshall    Edward    1903-03-14
# 2   b'b\x8ajP<\xbcc\xe0d\x1a\x9a^'      Billy   Jackson    1819-08-05
# 3   b'b\x8ajP<\xbcc\xe0d\x1a\x9a_'    Natalie  Cardwell    1896-10-02
# {'_id': array([b'b\x8ajP<\xbcc\xe0d\x1a\x9a\\', b'b\x8ajP<\xbcc\xe0d\x1a\x9a]',
#        b'b\x8ajP<\xbcc\xe0d\x1a\x9a^', b'b\x8ajP<\xbcc\xe0d\x1a\x9a_'],
#       dtype=object), 'first_name': array(['Andrew', 'Marshall', 'Billy', 'Natalie'], dtype='<U8'), 'last_name': array(['Simson', 'Edward', 'Jackson', 'Cardwell'], dtype='<U8'), 'date_of_birth': array(['2000-04-24T00:00:00.000', '1903-03-14T00:00:00.000',
#        '1819-08-05T00:00:00.000', '1896-10-02T00:00:00.000'],
#       dtype='datetime64[ms]')}
# -------------------------------------------------------------------------------------------------------------------------