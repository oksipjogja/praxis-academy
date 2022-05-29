from pymongo import MongoClient

client = MongoClient("mongodb+srv://oksip:umbara_77@oksiip.rbu8b8f.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_application

collection_name = db["todos_app"]
