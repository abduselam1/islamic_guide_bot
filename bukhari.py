import csv
from bs4 import BeautifulSoup
import requests
# abduCollection = MongoClient()
# quranDatabase = abduCollection.quran
# quran = quranDatabase.sura
baseUrl = "https://sunnah.com/bukhari:"

def get(hadithNumber):
    lists = []
    returnList = []
    # with open('hadith/sahih_al-bukhari_ahadith.utf8.csv',encoding='utf-8') as bukhari:
    #     bukhari = csv.reader(bukhari)
    #     # fields = next(bukhari)
    #     # print(bukhari)
    #     for hadith in bukhari:
    #         lists.append(hadith)

    #     # returnList.append(types.InlineQueryResultArticle(suras[sura][start-1]['verse'], suras[sura][start-1]['text'], types.InputTextMessageContent(verse['text'])))
    #     return lists[hadithNumber-1]
    #     # return returnList.append(types.InlineQueryResultArticle(lists[hadithNumber][0],lists[hadithNumber][0], "asdfasdfasdfadfadf adfjaskf"))
    source = requests.get(baseUrl+hadithNumber).text
    print('----')

    soup =  BeautifulSoup(source,'lxml')
    
    fullHadith ="",
    try:
        book_info = soup.find('div',class_="book_info")

        fullHadithContainer = soup.find('div',class_="AllHadith single_hadith")

        hadith = fullHadithContainer.find("div",class_="actualHadithContainer hadith_container_bukhari")


        allArabicHadithCollection = fullHadithContainer.find('div',class_="arabic_hadith_full arabic")

        lists = []
        detail = ""
        for spanHadith in allArabicHadithCollection.find_all('span'):
            detail = detail+spanHadith.text

        # for h in lists:
        #     fullHadith = fullHadith+h
        # fullHadith = lists[0]
        # fullHadith = fullHadith +lists[1]
        # fullHadith = fullHadith +lists[2]
        print(fullHadith)
        fullHadith = detail
    except Exception as e:
        raise e


    # if fullHadith == "":
    #     return None
    
    return fullHadith
    
    # return returnList

def getHadithFromOnline(hadithNumber):


    source = requests.get(baseUrl+hadithNumber).text
    
    soup =  BeautifulSoup(source,'lxml')
    kitabName = ""
    translatedKitabName=""
    babName = ""
    translatedBabName=""
    fullHadith ="",
    translatedHadith =""
    try:
        book_info = soup.find('div',class_="book_info")
        kitabName = book_info.find('div',class_="book_page_arabic_name arabic").text
        translatedKitabName = book_info.find('div',class_="book_page_english_name").text

        fullHadithContainer = soup.find('div',class_="AllHadith single_hadith")
        translatedBabName = fullHadithContainer.find('div',class_="englishchapter").text
        babName = fullHadithContainer.find('div',class_="arabicchapter arabic").text

        hadith = fullHadithContainer.find("div",class_="actualHadithContainer hadith_container_bukhari")

        translatedHadithCollection = fullHadithContainer.find('div',class_="english_hadith_full")

        narratedEng = translatedHadithCollection.find('div',class_="hadith_narrated")
        detailEng = translatedHadithCollection.find('div',class_="text_details")
        # print(narratedEng)
        narratedEngText = ""
        detailEngText = ""
        pOfDetialEng = detailEng.find_all('p')
        if narratedEng !=None:
            if narratedEng.find('p') == None:
                narratedEngText = narratedEng.text.strip()
            else:
                narratedEngText = narratedEng.find('p').text.strip()
            if len(detailEng.find_all('p')) == 0:
                detailEngText = detailEng.text.strip()
            else:
                for p in detailEng.find_all('p'):
                    detailEngText = detailEngText+p.text.strip()
                
        # print(detail)
        translatedHadith = narratedEngText +"\n" +detailEngText

        allArabicHadithCollection = fullHadithContainer.find('div',class_="arabic_hadith_full arabic")

        # allArabicHadithList = allArabicHadithCollection.find_all('span')
        # print(allArabicHadithList)
        lists = []
        spanHadiths = ""
        for spanHadith in allArabicHadithCollection.find_all('span'):
            spanHadiths = spanHadiths+spanHadith.text.strip()

        fullHadith = spanHadiths
        # for h in lists:
        #     fullHadith = fullHadith+h
        # fullHadith = lists[0]
        # fullHadith = fullHadith +lists[1]
        # fullHadith = fullHadith +lists[2]
        # print(kitabName)
        # print(translatedKitabName)
        # print(babName)
        # print(translatedBabName)
        # print(fullHadith)
    except Exception as e:
        print(e)


    if kitabName == "" or fullHadith == "" or babName == "":
        return []
    
    return [kitabName.strip(),translatedKitabName.strip(),babName.strip(),translatedBabName.strip(),fullHadith.strip(),translatedHadith.strip()]
    # print(translatedHadith)
    
    # print(soup.prettify())

# getHadithFromOnline('7')

# def get(sura,verse,user_id):
#     sura = quran.find_one({'id':sura})
#     return sura