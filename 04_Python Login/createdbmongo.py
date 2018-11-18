from pymongo import MongoClient
Client=MongoClient()
db=Client["Login"]
collection=db["Login_Details"]
log={}
log["UserName"]="test"
log["Password"]="dc06698f0e2e75751545455899adccc3"
collection.insert(log)
