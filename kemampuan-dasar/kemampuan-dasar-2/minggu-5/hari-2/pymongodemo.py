import pymongo

client = pymongo.MongoClient()
print(client.list_database_names()) # ----> menampilkan list database (show dbs/dlm terminal mongo)

# MEMBUAT DATABASE DAN MEMBUAT COLLECTION SERTA INSERT 
# mydb = client["mydb"]

# mycol = mydb["kampung"]

# data = {'nama': 'ipoel', 'usia': 35}
# mycol.insert_one(data)


# datalist = [{'nama' : 'gunawan', 'usia': 32}, {'nama': 'wawan', 'usia': 45}, {'nama': 'nuri', 'usia': 32}]
# mycol.insert_many(datalist)


