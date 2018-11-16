import pymongo
import hashlib
print("##########  User Login  ##########")
un=input("enter User Name : ")
pwd=hashlib.md5(input("enter Password : ").encode()).hexdigest()
uri="mongodb://127.0.0.1:27017"
client=pymongo.MongoClient(uri)
database=client['Login']
collection=database['Login_Details']
users=collection.find({})
for user in users:
    if un==user['UserName'] and pwd==user['Password']:
        print("$$$ Successful Loged IN $$$")
        print("Hello "+un)
    else:
        print("UserName Or Password Incorrect")







 
