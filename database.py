from pymongo import MongoClient

client = MongoClient("your mongo url")
db = client["students"]
collection = db["students"]
