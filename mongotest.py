import pymongo
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://ineuron:Sushant123@sushant.jo4faz9.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
client = MongoClient(uri)
print(client)


d = {
    "name": "sudhanshu",
    "emailid": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}

client1 = client['mongotest']
coll = client1['test']
coll.insert_one(d)
