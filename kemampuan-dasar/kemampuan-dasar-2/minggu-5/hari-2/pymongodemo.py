from argparse import _MutuallyExclusiveGroup
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

# ---- melakukan looping dari database ----
mydb=client['OKSIPJOGJA']
mycol  = mydb['DtlCont']
for x in mycol.find({"jumlah anak":{"$gte" : "3"}}):
    print(x)
# # outputnya ---> ['OKSIPJOGJA', 'admin', 'config', 'local', 'mydb']
# {'_id': ObjectId('627f24bae6dc335eeff9c2af'), 'nama': 'Kenthir Widodo', 'alamat ': 'jalan senopati no 15 yogyakarta', 'pekerjaan': 'PNS', 'jumlah anak': '3', 'penghasilan': '5000000'}
# {'_id': ObjectId('627f24bae6dc335eeff9c2b1'), 'nama': 'Bandot Pamuji', 'alamat ': 'jalan roesman no 9 yogyakarta', 'pekerjaan': 'PNS', 'jumlah anak': '5', 'penghasilan': '8000000'}
    
mydb = client["OKSIPJOGJA"]
mycol = mydb["DtlCont"]
# for x in mycol.find():
#     print(x)
# outputnya ---> ['OKSIPJOGJA', 'admin', 'config', 'local', 'mydb']
# {'_id': ObjectId('627f24bae6dc335eeff9c2af'), 'nama': 'Kenthir Widodo', 'alamat ': 'jalan senopati no 15 yogyakarta', 'pekerjaan': 'PNS', 'jumlah anak': '3', 'penghasilan': '5000000'}
# {'_id': ObjectId('627f24bae6dc335eeff9c2b1'), 'nama': 'Bandot Pamuji', 'alamat ': 'jalan roesman no 9 yogyakarta', 'pekerjaan': 'PNS', 'jumlah anak': '5', 'penghasilan': '8000000'}
# {'_id': ObjectId('627f24bae6dc335eeff9c2af'), 'nama': 'Kenthir Widodo', 'alamat ': 'jalan senopati no 15 yogyakarta', 'pekerjaan': 'PNS', 'jumlah anak': '3', 'penghasilan': '5000000'}
# {'_id': ObjectId('627f24bae6dc335eeff9c2b0'), 'nama': 'Waluyo Pangarep', 'alamat ': 'Jalan maespati no 25B yogyakarta', 'pekerjaan': 'wiraswasta', 'jumlah anak': '2', 'penghasilan': '3000000'}
# {'_id': ObjectId('627f24bae6dc335eeff9c2b1'), 'nama': 'Bandot Pamuji', 'alamat ': 'jalan roesman no 9 yogyakarta', 'pekerjaan': 'PNS', 'jumlah anak': '5', 'penghasilan': '8000000'}
# {'_id': ObjectId('627f24bae6dc335eeff9c2b2'), 'nama': 'Dobol Permadi', 'alamat ': 'jalan ibu dahlan no 90 yogyakarta', 'pekerjaan': 'Seniman', 'jumlah anak': '1', 'penghasilan': '4000000'}
# {'_id': ObjectId('627f24bae6dc335eeff9c2b3'), 'nama': 'Bagus Triatmojo', 'alamat ': 'jalan surabaya no 45 yogyakarta', 'pekerjaan': 'Seniman', 'jumlah anak': '2', 'penghasilan': '9000000'}
# {'_id': ObjectId('627f24bae6dc335eeff9c2b4'), 'nama': 'Djumadi Sumitro', 'alamat ': 'jalan solo no 85 yogyakarta', 'pekerjaan': 'Karyawan', 'jumlah anak': '1', 'penghasilan': '5000000'}
# {'_id': ObjectId('627f24bae6dc335eeff9c2b5'), 'nama': 'Djulianto Ramadani', 'alamat ': 'jalan magelang no 38 yogyakarta', 'pekerjaan': 'Karyawan', 'jumlah anak': '2', 'penghasilan': '4500000'}
# {'_id': ObjectId('627f24bae6dc335eeff9c2b6'), 'nama': 'Sumardi Duldani', 'alamat ': 'jalan demangan no 21 yogyakarta', 'pekerjaan': 'PNS', 'jumlah anak': '1', 'penghasilan': '3000000'}

for x in mycol.find({"pekerjaan":"PNS"}):
    print(x)