import json
import telebot
import bukhari
import muslim
import quran
import functions
from telebot import types
logger = telebot.logger

bot = telebot.TeleBot("5021378171:AAFEAXPE544xZELUse5kqZMo9I2Mm4RrPVE", parse_mode=None)

report = {}



@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document'])
def default_command(message):
    print(message.id)
    print(message.chat.id)
    
    # bot.forward_message(5422471566,-1001860136079,29)
    bot.send_message(message.chat.id, message.chat.id)
    

@bot.message_handler(func=lambda message: message.text == "hello")
def echo_all(message):
	bot.send_audio(message.chat.id, "http://www.everyayah.com/data/Hudhaify_64kbps/001002.mp3")

@bot.message_handler(func=lambda message: message.text.lower().startswith('bukhari '))
def send_quran(message):
    splitedData = message.text.split()
    hadiths = bukhari.getHadithFromOnline(splitedData[1])
    if len(hadiths) == 0:
        bot.send_message(message.chat.id,"Make sure you type the correct hadith number like this \nBukhari 13")
    else:
        fullArabic = hadiths[0]+'\n\n'+hadiths[2]+"\n\n"+splitedData[1]+'. '+ hadiths[4]+"\n\n صحيح البخاري"
        FullEng = "Book of "+hadiths[1]+'\n\n'+hadiths[3]+"\n\n"+splitedData[1]+'. '+ hadiths[5]+"\n\n Sahih Bukhari"
        fullHadith = fullArabic+"\n\n\n"+FullEng
        if len(fullHadith) > 4096:
            for x in range(0, len(fullHadith), 4096):
                bot.send_message(message.chat.id, fullHadith[x:x+4096])
            else:
                bot.send_message(message.chat.id, fullHadith)
        bot.send_message(message.chat.id,fullHadith)
    # bot.send_audio(message.chat.id,'https://download.quranicaudio.com/quran/abdullaah_3awwaad_al-juhaynee/112.mp3',title="fatiha")

@bot.message_handler(func=lambda message: message.text.lower().startswith('muslim '))
def send_quran(message):
    splitedData = message.text.split()
    hadiths = muslim.getHadithFromOnline(splitedData[1])
    if len(hadiths) == 0:
        bot.send_message(message.chat.id,"Make sure you type the correct hadith number like this \nMuslim 13")
    else:
        fullArabic = hadiths[0]+'\n\n'+hadiths[2]+"\n\n"+splitedData[1]+'. '+ hadiths[4]+"\n\n صحيح مسلم"
        FullEng = "Book of "+hadiths[1]+'\n\n'+hadiths[3]+"\n\n"+splitedData[1]+'. '+ hadiths[5]+"\n\n Sahih Muslim"
        fullHadith = fullArabic+"\n\n\n"+FullEng
        if len(fullHadith) > 4096:
            for x in range(0, len(fullHadith), 4096):
                bot.send_message(message.chat.id, fullHadith[x:x+4096])
            else:
                bot.send_message(message.chat.id, fullHadith)
        bot.send_message(message.chat.id,fullHadith)
    # bot.send_audio(message.chat.id,'https://download.quranicaudio.com/quran/abdullaah_3awwaad_al-juhaynee/112.mp3',title="fatiha")

def quranMarkup(sura,verse):
    markup = types.InlineKeyboardMarkup()

    my3Button = types.InlineKeyboardButton("mp3",callback_data="mp3"+functions.formatAyahForAudio(int(sura))+functions.formatAyahForAudio(int(verse)))
    tranEng = types.InlineKeyboardButton("Translate En",callback_data="tran-en "+sura+':'+verse)
    tranFra = types.InlineKeyboardButton("Translate Fr",callback_data="tran-fr "+sura+':'+verse)
    tranEsp = types.InlineKeyboardButton("Translate Es",callback_data="tran-es "+sura+':'+verse)

    markup.row(my3Button)

    markup.row(tranEng,tranFra,tranEsp)

    return markup


@bot.message_handler(func=lambda message: message.text.lower().startswith('quran '))
def send_quran(message):
    getVerse = message.text.split()

    verse="0"
    
    sura = "0";

    if(len(getVerse) != 1):
        separateSuraFromVerse = getVerse[1].split(':')
        sura = separateSuraFromVerse[0]
        if (len(separateSuraFromVerse) != 1):
            verse = separateSuraFromVerse[1]
            totalVerse = quran.getSingleAyah(sura,int(verse))
            if totalVerse == None:
                bot.send_message(message.chat.id,"Make sure you type the correct Quran sura and ayah number like this \nQuran sura:ayah (Quran 2:255)")
            else:
                
                # bukhari = types.InlineKeyboardButton("Bukhari",callback_data="bukhari")
                # muslim = types.InlineKeyboardButton("muslim",callback_data="muslim")



                bot.send_message(message.chat.id, totalVerse,reply_markup=quranMarkup(sura,verse))

        else:
            bot.send_message(message.chat.id,"Make sure you type the correct Quran sura and ayah number like this \nQuran sura:ayah (Quran 2:255)")

    # hadiths = muslim.getHadithFromOnline(splitedData[1])
    else:
        bot.send_message(message.chat.id,"Make sure you type the correct Quran sura and ayah number like this \nQuran sura:ayah (Quran 2:255)")
        # bot.send_audio(message.chat.id,'https://download.quranicaudio.com/quran/abdullaah_3awwaad_al-juhaynee/112.mp3',title="fatiha")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data.startswith('help'):
        helpType = call.data.split()
        if helpType[1] == 'inline':
            bot.forward_message(call.from_user.id,-1001860136079,33)
            bot.forward_message(call.from_user.id,-1001860136079,35)
            bot.forward_message(call.from_user.id,-1001860136079,37)
            bot.forward_message(call.from_user.id,-1001860136079,52)
        elif helpType[1] == "full":
            bot.forward_message(call.from_user.id,-1001860136079,54)
            bot.forward_message(call.from_user.id,-1001860136079,55)
            bot.forward_message(call.from_user.id,-1001860136079,56)
    if call.data.startswith("mp3"):
        
        ayah = call.data.removeprefix('mp3')
        print('ayah')
        bot.send_audio(call.from_user.id, "http://www.everyayah.com/data/Hudhaify_64kbps/"+ayah+".mp3")

        # bot.answer_callback_query(call.id, "Answer is"+ayah)
    if call.data.startswith('tran'):
        # bot.answer_callback_query(call.id, call.data)
        separateTranslationFromSura = call.data.split()
        lang = separateTranslationFromSura[0].split('-')[1]
        suraAndVerse = separateTranslationFromSura[1].split(':')

        bot.edit_message_text(quran.translateAyah(int(suraAndVerse[0]),int(suraAndVerse[1]),lang),call.from_user.id,call.message.id,reply_markup=quranMarkup(suraAndVerse[0],suraAndVerse[1]))
        # bot.answer_callback_query(call.id, lang)
    # elif call.data == "bukhari":
    #     bot.answer_callback_querNy(call.id, "Answer is bukhari")
    # elif call.data == "muslim":
    #     print(call)
    #     bot.answer_callback_query(call.id, call.id)



@bot.message_handler(func=lambda message: message.text == 'mp3')
def send_quran(message):
    
    print(message.id)
    # bot.forward_message(5422471566,446003817,286)
    # bot.send_message(message.chat.id,message.id)
    # bot.send_audio(message.chat.id,'https://download.quranicaudio.com/quran/abdullaah_3awwaad_al-juhaynee/112.mp3',title="fatiha")

@bot.message_handler(commands='start')
def echo_all(message):
    markup = types.InlineKeyboardMarkup()

    quran_button = types.InlineKeyboardButton("Quran",switch_inline_query_current_chat=" .quran")
    bukhari = types.InlineKeyboardButton("Bukhari",switch_inline_query_current_chat=" .bukhari")
    muslim = types.InlineKeyboardButton("Muslim",switch_inline_query_current_chat=" .muslim")
    
    markup.row(quran_button)

    markup.row(muslim,bukhari)
    
    print(message.chat.id)
    # functions.registerUser(message=message)
    # bot.send_message(message.chat.id,message.id)
    bot.send_message(message.chat.id,"A bot with multiple useful functionality for all muslims \n\n1. search for quran verses \n2. Search for Sahih bukhari hadith \n3.Search for Sahih muslim hadith \n\n And more to come soon",reply_markup=markup,)

@bot.inline_handler(lambda query: True)
def query_text(inline_query):
    print(inline_query.query)
    if inline_query.query.startswith('.quran'):
        try:
            # verse
            # result = quran.get(1,1,00)
            getVerse = inline_query.query.split()
            startVerse="0"
            endVerse = "0"
            sura = "0"

            if(len(getVerse) != 1):
                separateSuraFromVerse = getVerse[1].split(':')
                sura = separateSuraFromVerse[0]
                if (len(separateSuraFromVerse) != 1):
                    separateVerses= separateSuraFromVerse[1].split('-')
                    startVerse = separateVerses[0]
                    if(len(separateVerses) != 1):
                        endVerse = separateVerses[1]
            
            # print("=======")
            # print(sura)
            # print("------")

            # print(endVerse)
            
            totalResult = quran.get(sura,int(startVerse),int(endVerse))
            inlineMessage = totalResult[0]

            # print(inlineMessage)
            options = []
            if len(totalResult) == 2:
                options.append(types.InlineQueryResultArticle(startVerse+'-'+endVerse, "All verses", types.InputTextMessageContent(totalResult[1]+ "\n\n Quran "+sura+':'+startVerse+"-"+endVerse)))
            for verse in inlineMessage:
                options.append(types.InlineQueryResultArticle(verse['verse'], str(verse['verse'])+'. '+verse['text'], types.InputTextMessageContent(str(verse['verse'])+'. '+verse['text']+" \n\n Quran "+str(verse['chapter'])+':'+str(verse['verse']))))
            # r = types.InlineQueryResultArticle('1', 'Result quan dafjk  ', types.InputTextMessageContent('Result message quran.'))
            # r2 = types.InlineQueryResultArticle('2', 'Result quran 2', types.InputTextMessageContent('Result message2 quran.'))
            bot.answer_inline_query(inline_query.id, options)
        except Exception as e:
            print(e)
    elif inline_query.query.startswith('.bukhari'):
        try:
            print('hgjh')
            getHadithNumber = inline_query.query.split()
            hadith = []
            if(len(getHadithNumber) != 1):
                
                full_hadith = bukhari.get(getHadithNumber[1])
                print(full_hadith)
                if len(full_hadith) > 2048:
                    print("long")

                    hadith.append(full_hadith[0:2048])
                    hadith.append(full_hadith[2048:])
                returnedList = []
                print(len(hadith))
                if(len(hadith) > 0):
                    returnedList.append(types.InlineQueryResultArticle(getHadithNumber[1], hadith[0], types.InputTextMessageContent(getHadithNumber[1]+'. '+hadith[0]+'...')))
                    returnedList.append(types.InlineQueryResultArticle('...', hadith[1], types.InputTextMessageContent('...'+hadith[1]+'\n\n Sahih Bukahri hadith - '+getHadithNumber[1])))
                else:
                    returnedList.append(types.InlineQueryResultArticle(getHadithNumber[1], full_hadith, types.InputTextMessageContent(getHadithNumber[1]+'. '+full_hadith+'\n\n Sahih Bukahri hadith - '+getHadithNumber[1])))

                # for had in hadith:
                bot.answer_inline_query(inline_query.id, returnedList)

            # r2 = types.InlineQueryResultArticle('2', 'bukhari 2', types.InputTextMessageContent('Result message2 quran.'))
            # bot.answer_inline_query(inline_query.id, [r, r2])
        except Exception as e:
            print(e)
    elif inline_query.query.startswith('.muslim'):
        try:
            print('muslim')
            getHadithNumber = inline_query.query.split()
            hadith = []
            if(len(getHadithNumber) != 1):
                
                full_hadith = muslim.get(getHadithNumber[1])
                print(full_hadith)
                if len(full_hadith) > 2048:
                    print("long")

                    hadith.append(full_hadith[0:2048])
                    hadith.append(full_hadith[2048:])
                returnedList = []
                print(len(hadith))
                if(len(hadith) > 0):
                    returnedList.append(types.InlineQueryResultArticle(getHadithNumber[1], hadith[0], types.InputTextMessageContent(getHadithNumber[1]+'. '+hadith[0]+'...')))
                    returnedList.append(types.InlineQueryResultArticle('...', hadith[1], types.InputTextMessageContent('...'+hadith[1]+'\n\n Sahih Bukahri hadith - '+getHadithNumber[1])))
                else:
                    returnedList.append(types.InlineQueryResultArticle(getHadithNumber[1], full_hadith, types.InputTextMessageContent(getHadithNumber[1]+'. '+full_hadith+'\n\n Sahih Bukahri hadith - '+getHadithNumber[1])))

                # for had in hadith:
                bot.answer_inline_query(inline_query.id, returnedList)

            # r2 = types.InlineQueryResultArticle('2', 'bukhari 2', types.InputTextMessageContent('Result message2 quran.'))
            # bot.answer_inline_query(inline_query.id, [r, r2])
        except Exception as e:
            print(e)

@bot.message_handler(commands='help')
def helpHandler(message):
    print(message.chat)
    
    markupInline = types.InlineKeyboardMarkup()
    markupFull = types.InlineKeyboardMarkup()
    my3Button = types.InlineKeyboardButton("Show me By Picture",callback_data="help inline")
    fullButon = types.InlineKeyboardButton("Show my by picture",callback_data="help full")

    markupInline.row(my3Button)
    markupFull.row(fullButon)
    # bot.send_message(message.chat.id,"Here is a sample pictures to follow on searching inline query( you can use it in any chat)")
    bot.send_message(message.chat.id,"Our bot gives a lot of features like searching for quran verse, Sahih Bukhari and muslim with and without translation \n\n When you need to use inline query( You can use it in any chat you need ) \nFor Quran type  @islamicGuideBot .quran 2:255\nFor Bukhari  @islamicGuideBot .bukhari n (n=Hadith number)\nFor muslim  @islamicGuideBot .muslim n (n=Hadith number)",reply_markup=markupInline)
    bot.send_message(message.chat.id,"If you need more features just send us the Quran verse you need like\n\nQuran 2:255\nFor Bukhari  Bukhari n (n=Hadith number)\nFor muslim Muslim n (n=Hadith number)",reply_markup=markupFull)
    

@bot.message_handler(commands='report')
def askQuestionHandler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard = generateKeyboard([])

    markup.row(types.KeyboardButton('🪲 Bug'),types.KeyboardButton('⬆️ Improvement'))
    markup.row(types.KeyboardButton('❌ Cancel'))
    ask_question_message = bot.send_message(message.chat.id,"Choose report type",reply_markup=markup)
    bot.register_next_step_handler(ask_question_message, handleReportType)

def handleReportType(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    close = types.KeyboardButton('❌ Cancel')
    markup.row(close)
    if message.text == '❌ Cancel':
        bot.send_message(message.chat.id,"Canceled the process",reply_markup=types.ReplyKeyboardRemove())
        # send_welcome(message)
    elif message.text == '🪲 Bug':
        report['type'] = "Bug report"
        select_detail_message = bot.send_message(message.chat.id, "Tell us what error you get...", reply_markup=markup)
        bot.register_next_step_handler(select_detail_message, handleContent)

    else:
        report['type'] = "Improvement"
        select_detail_message = bot.send_message(message.chat.id, "Tell us what you have on your mind...", reply_markup=markup)
        bot.register_next_step_handler(select_detail_message, handleContent)

def handleContent(message):
    if message.text == '❌ Cancel':
        bot.send_message(message.chat.id,"Canceled the process",reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(5422471566,report['type']+"\nFrom username: "+str(message.chat.username)+"\nId: "+str(message.chat.id)+"\nFull name: "+message.chat.first_name+" \n\n "+message.text)

    bot.send_message(message.chat.id,"Thanks for reaching to us",reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands='comment')
def askQuestionHandler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard = generateKeyboard([])

    # markup.row(types.KeyboardButton('🪲 Bug'),types.KeyboardButton('⬆️ Improvement'))
    markup.row(types.KeyboardButton('❌ Cancel'))
    write_comment = bot.send_message(message.chat.id,"Write your comment",reply_markup=markup)
    bot.register_next_step_handler(write_comment, handleComment)

def handleComment(message):
    if message.text == '❌ Cancel':
        bot.send_message(message.chat.id,"Canceled the process",reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(5422471566,"Commment: "+"\nFrom username: "+str(message.chat.username)+"\nId: "+str(message.chat.id)+"\nFull name: "+message.chat.first_name+" \n\n "+message.text)

    bot.send_message(message.chat.id,"Thanks for reaching to us we will reply ASAP",reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(func= lambda message: message.text.startswith('aaa'))
def testFromLocal(message):
    with open('hadith/sahih_bukhari.json',encoding="utf-16") as hadith:
        # print(hadith)
        jsond = json.load(hadith)
        print(jsond[0]['kitabName'])
        bot.send_message(message.chat.id,jsond[0]['fullHadith'])
# @bot.inline_handler(lambda query: True)
# def query_text(inline_query):
#     try:
#         r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
#         r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
#         print('hello')
#         bot.answer_inline_query(inline_query.id, [r, r2])
        
#     except Exception as e:
#         print(e)



bot.infinity_polling(interval=0, timeout=30)