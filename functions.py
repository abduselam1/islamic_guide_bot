from pymongo import MongoClient
# import json
# from json import decoder
# import os
# abduCollection = MongoClient("mongodb+srv://root:Abdu.mongodb21@abdu.qaadv.mongodb.net/IslamicGuide?retryWrites=true&w=majority",serverSelectionTimeoutMS=10000)
client = MongoClient("mongodb+srv://root:Abdu.mongodb21@abdu.qaadv.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# mongo = MongoClient()
quranDatabase = client.IslamicGuide
userCollection = quranDatabase.users
def registerUser(message):
    print(userCollection)
    # id = message.chat.id
    user = userCollection.find_one(filter={'chat_id':message})
    if True:
        print(message.chat)
        user = {
            "chat_id": "344",
            "username": "abdu_curry",
            "first_name": "abdu",
            "translation": 'en'
        }
        userCollection.insert_one(user)
    else:
        print('found')

def formatAyahForAudio(number):
    if(number < 9):
        return '00'+str(number)
    elif number < 99:
        return "0"+str(number)
    else:
        return str(number)