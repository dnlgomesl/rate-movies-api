import pymongo

MONGO_CLIENT = pymongo.MongoClient("mongodb://mongo:27017")

DB = MONGO_CLIENT.Movies