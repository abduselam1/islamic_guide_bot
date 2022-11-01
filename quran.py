import json
# abduCollection = MongoClient()
# quranDatabase = abduCollection.quran
# quran = quranDatabase.sura

def get(sura,start,end):
    returnList = []
    allAyah = ""
    with open('quran/quran.json',encoding='utf-8') as quran:
        suras = json.load(quran)
        
        if((start > end and end == 0 ) or start <= end):
            if(end !=  0):
                # print('here')
                original = suras[sura][start-1:end]
                
                for verse in original:
                    # returnList.append(types.InlineQueryResultArticle(verse['verse'], verse['text'], types.InputTextMessageContent(verse['text'])))
                    allAyah += str(verse['verse'])+'. '+verse['text']+'\n'
                    returnList.append(verse)
                # print(allAyah)
                # returnList.append({'chapter':int(sura),'verse':'All\n','text':allAyah})
            else:
                if(start == 0):
                    start += 1
                
                # original = 
                # returnList.append(types.InlineQueryResultArticle(suras[sura][start-1]['verse'], suras[sura][start-1]['text'], types.InputTextMessageContent(verse['text'])))
                # print()
                returnList.append(suras[sura][start-1])

    # print(returnList)
    if allAyah != "":
        return [returnList,allAyah]
    return [returnList]
    
def getSingleAyah(sura,ayah):
    ayahToReturn = ''
    with open('quran/quran.json',encoding='utf-8') as quran:
        suras = json.load(quran)
          
        try:
            if(ayah == 0):
                ayah += 1
            
            
            # print(sura[])
            ayahToReturn = suras[sura][ayah-1]['text']
        except Exception as e:
            ayahToReturn = None

    # print(returnList)
    return ayahToReturn


def getSingleAyah(sura,ayah):
    ayahToReturn = ''
    with open('quran/quran.json',encoding='utf-8') as quran:
        suras = json.load(quran)
          
        try:
            if(ayah == 0):
                ayah += 1
            
            
            # print(sura[])
            ayahToReturn = str(ayah)+'. '+suras[sura][ayah-1]['text']
        except Exception as e:
            ayahToReturn = None

    # print(returnList)
    return ayahToReturn

def translateAyah(sura,ayah,code):
    ayahToReturn = ''
    with open('quran/quran_'+code+'.json',encoding='utf-8') as quran:
        suras = json.load(quran)
          
        try:
            if(ayah == 0):
                ayah += 1
            
            
            # print(sura[])
            fullSura = suras[sura-1]
            ayahToReturn = fullSura['name']+'\n'+ str(ayah)+'. '+ fullSura['verses'][ayah-1]['text'] +'\n\n\n'
            ayahToReturn += fullSura['transliteration']+'\n'+str(ayah)+'. '
            ayahToReturn += fullSura['verses'][ayah-1]['translation']
            # print(fullSura)
        except Exception as e:
            ayahToReturn = None

    # print(returnList)
    return ayahToReturn
# def get(sura,verse,user_id):
#     sura = quran.find_one({'id':sura})
#     return sura