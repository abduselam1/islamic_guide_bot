from pymongo import MongoClient
import json
from json import decoder
import os
# abduCollection = MongoClient("mongodb+srv://root:Abdu.mongodb21@abdu.qaadv.mongodb.net/IslamicGuide?retryWrites=true&w=majority",serverSelectionTimeoutMS=10000)
# mz1XBTiU3hg4GsDS
abduCollection = MongoClient()
quranDatabase = abduCollection.quran
translationCollection = quranDatabase.translation
# print(abduCollection.list_database_names())
# try:
#     print(abduCollection.server_info())
# except Exception:
#     print("Unable to connect to the server.")

# with open('quran.json',encoding='utf-8') as quran:
#     suras = json.load(quran)
# with open('quran_en.json',encoding='utf-8') as quran:
#     quran_en = json.load(quran)
# with open('quran_fr.json',encoding='utf-8') as quran:
#     quran_fr = json.load(quran)
# with open('quran_es.json',encoding='utf-8') as quran:
#     quran_es = json.load(quran)
# with open('quran_tr.json',encoding='utf-8') as quran:
#     quran_tr = json.load(quran)
# with open('quran_ur.json',encoding='utf-8') as quran:
#     quran_tr = json.load(quran)
# with open('quran_id.json',encoding='utf-8') as quran:
#     quran_tr = json.load(quran)

# translation = quranDatabase.translation
# for index in range(114):
    

# translation = [
#     {
#         "id":114,
#         "name":{
#             "en":"Mankind",
#             "fr":"Les humains"
#             },
#         "verses":[
#             {
#                 'id':0,
#                 "text":{
#                     "fr":"Dis: «Je cherche protection auprès du Seigneur des hommes",
#                     "en":"Say, \"I seek refuge in the Lord of mankind"
#                     }
#             }
#         ]
#     }
# ]
# print(len(suras))
# for su in suras:
#     sura.insert_one(su)
# sura.insert_many(sura)

# for i in range(114):
#     if i < 20:
#         continue
#     sura.insert_one(suras[i])

files = os.listdir()
for index in range(114): # there are 114 sura so we iterate and work with every sura
    data = {}
    
    for file in files:
        if file.endswith('.json'):
            
            file_name = file.removesuffix('.json')
            language = file_name.split('_')[1]
            with open(file,encoding="utf-8") as translation:
                decoded_translation = json.load(translation)
                #catching the sura using index
                current_sura = decoded_translation[index]
                data['id'] = current_sura['id']
                data['name'] = current_sura['name']
                data['transliteration'] = current_sura['transliteration']
                data['type'] = current_sura['type']
                data['total_verses'] = current_sura['total_verses']
                if "translation" not in data.keys():
                    data['translation'] = {language:current_sura['translation']}
                else:
                    name_translation = data['translation']
                    name_translation[language] = current_sura['translation']
                    data['translation'] = name_translation
                # iteratre over verses
                translated_verse = []
                if 'verses' not in data.keys():
                    
                    for verse in current_sura['verses']:
                        # print(verse)
                        each_verse = {
                            "id": verse['id'],
                            "text":{
                                language:verse['translation']
                            } 
                        }
                        translated_verse.append(each_verse)
                    data['verses'] = translated_verse
                else:
                    
                    for verse in current_sura['verses']:
                        # previouse_data = data['verses'][verse.id]['text']
                        data['verses'][verse['id']-1]['text'][language] = verse['translation']
                        # translated_verse.append(verse['translation'])
    translationCollection.insert_one(data)           


                    
            
