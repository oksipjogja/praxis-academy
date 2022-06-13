from dotenv import load_dotenv, find_dotenv 
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")


connection_string = f"mongodb+srv://oksipjogja:{password}@cluster0.2bla9.mongodb.net/?retryWrites=true&w=majority&authSource=admin"

client = MongoClient(connection_string)

dbs = client.list_database_names()
sekolah = client.sekolah

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

def create_guru_collection():
  guru_validator = {
    "$jsonSchema": {
      "bsonType": "object",
      "required": [ "first_name", "last_name", "mobile_phone", "date_of_birth" ],
      "properties": {
          "first_name": {
            "bsonType": "string",
            "description": "must be a string and is required"
          },
          "last_name": {
            "bsonType": "string",
            "description": "must be a string and is required"
          },
          "mobile_phone": {
            "bsonType": "string",
            "description": "must be a string and is required"
          },
          "date_of_birth": {
            "bsonType": "date",
            "description": "must be a date and is required"
          },           
        }
      }
    }
  
  try:
    sekolah.create_collection("guru")
  except Exception as e:
    print(e)   

  sekolah.command("collMod", "guru", validator=guru_validator)

create_guru_collection()
   




















# publisher = client.publisher

# validator = {
#     "$jsonSchema": {
#         "bsonType": "object",
#         "required": [ "title", "authors", "publish_date", "type", "copies" ],
#         "properties": {
#           "title": {
#               "bsonType": "string",
#               "description": "must be a string and is required"
#           },
#           "authors": {
#               "bsonType": "array",
#               "items": {
#                 "bsonType": "objectId",
#                 "description": "must be a objectid and is required"
#               }              
#           },
#           "publish_date": {
#               "bsonType": "date",
#               "description": "must be a date an is required"
#           },
#           "type": {
#               "enum": [ "Fiction", "Non-Fiction" ],
#               "description": "can only be one of the enum values and is required"
#           },
#           "copies": {
#               "bsonType": "int",
#               "minimum": "0",
#               "description": "must be an integer greater than 0 and is required"
#           },
#         }
#     }
# }
                                    
# try:
#   publisher.create_collection("book")
# except Exception as e:
#   print(e)   

# publisher.command("collMod", "book", validator=validator)