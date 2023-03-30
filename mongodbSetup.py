import pymongo
import certifi

ca = certifi.where()

mongoClient = pymongo.MongoClient("mongodb+srv://root:rDKHjyi2yMhTFeQF@project-phase-3-db.vhxffza.mongodb.net/?retryWrites=true&w=majority"
                                  ,tlsCAFile=ca)	

db = mongoClient["project-phase-3-db"]


print("Sucessfully connected to mongo db.")
