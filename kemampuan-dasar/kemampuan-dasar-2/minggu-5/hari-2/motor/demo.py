import pymongo

client = pymongo.MongoClient("store")
print(client.list_database_names()) 




