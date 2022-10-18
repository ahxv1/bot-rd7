import types
import telebot
from telebot import * 
import random

token ="1995113388:AAFQMJCv5t3Ai7oiBqlNuf36q4H7P4HtF7o"
bot =telebot.TeleBot(token)



@bot.message_handler(commands=["start"])
def st(message):
    key = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text="الاوامر",callback_data="a")
    but2 = types.InlineKeyboardButton(text="المبرمج",url="instagram.com/t.9j_")
    key.add(but1,but2)
    bot.reply_to(message,"""مرحبا بك في بوت (حمود) انا بوت متخصص في القروبات العامة من اهم مميزاتي : 

1- امكانية طرد اعضاء في القروب معينين
2- ارسال نكت و ميمز 
3- التفاعل مع اعضاء القروب """,reply_markup=key)


@bot.message_handler(func=lambda rep : True)
def reply(rep):
    #reply
    ran = ("عيونه","هلا","ارححب")

    if rep.text == "السلام عليكم":
        bot.reply_to(rep,"وعليكم السلام")

    elif rep.text ==  "حمود":
        bot.reply_to(rep,random.choice(ran))

    elif rep.text == "احبك":
        bot.reply_to(rep,"انا اكثر والله")



@bot.callback_query_handler(func=lambda c : True)
def call(c):
    if c.data == "a":
        tex = """1- السلام عليكم
        2- حمود
        3- الطرد يمكنك استخدامه بالرد على رسالة الشخص الذي تريد طرده ثم تكتب طرد 
        """
        bot.send_message(c.message.chat.id,tex)



bot.infinity_polling()