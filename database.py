from pymongo import MongoClient

client = MongoClient("mongodb+srv://divyanshu:divyanshu@cluster0.57fvbtj.mongodb.net/")
db = client["students"]
collection = db["students"]