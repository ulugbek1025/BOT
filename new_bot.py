import telebot
from telebot import types
from string import Template
bot=telebot.TeleBot('1648785365:AAE3i1nDRp9xjBtDkCrl9S2OmAoiCSZH_MI')
user_dict = {}

class User:
    def __init__(self,city):
        self.city=city

        keys = ['jins','FIO','yosh','phone',
                'tuman','manzil','malumot',
                'soha']

        for key in keys:
            self.key=None

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    itembtn1=types.KeyboardButton('/About')
    itembtn2=types.KeyboardButton('/Registartiya')
    itembtn3=types.KeyboardButton('/Manzil')
    
    markup.add(itembtn1,itembtn2,itembtn3) 
    msg = bot.reply_to(message, 'Assalamu aleykum '+ message.from_user.first_name+'\n Jondor IT CENTERning rasmiy botiga xush kelibsiz', reply_markup=markup)




@bot.message_handler(commands=['About'])
def send_welcome(message):
    msg = bot.reply_to(message, "Raqamli texnologiyalar o'quv markazlari\n"
                                +"Created by Ulug'bek\n"+
                                " jondor-rtm.uz\n"+
                                "+998936541025")

@bot.message_handler(commands=['Manzil'])
def send_welcome(message):
    msg = bot.reply_to(message, "Buxoro viloyat\n "
                                +"Jondor tuman\n"+
                                "49-maktab binosi")

#reg/

@bot.message_handler(commands=['Registartiya'])
def user_reg(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembnt1=types.KeyboardButton('erkak')
    itembnt2=types.KeyboardButton('ayol')
    markup.add(itembnt1,itembnt2)
    msg = bot.send_message(message.chat.id, 'Jinsingiz', reply_markup=markup)
    bot.register_next_step_handler(msg, process_jins_step)
    
    
def process_jins_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'FIO', reply_markup=markup)
        
        bot.register_next_step_handler(msg, process_FIO_step)
    except Exception as e:
       bot.reply_to(message, 'ooops!!')



def process_FIO_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.FIO = message.text
        
        msg = bot.send_message(chat_id, 'Yosh kiriting')
        bot.register_next_step_handler(msg, process_yosh_step)

    except Exception as e:
       bot.reply_to(message, 'ooops!!')



def process_yosh_step(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.yosh = message.text

        msg = bot.send_message(chat_id, 'Telefon raqam')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        msg = bot.reply_to(message, 'son kiriting')
        bot.register_next_step_handler(msg, process_yosh_step)



def process_phone_step(message):
    
    try:
        int(message.text)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text
        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembnt1=types.KeyboardButton('Jondor')
        itembnt2=types.KeyboardButton('Buxoro')
        itembnt3=types.KeyboardButton('Buxoro sh')
        itembnt4=types.KeyboardButton("Qorako'l")
        itembnt5=types.KeyboardButton('Olot')
        itembnt6=types.KeyboardButton('Peshku')
        itembnt7=types.KeyboardButton('Gijduvon')
        itembnt8=types.KeyboardButton('Rominat')
        itembnt9=types.KeyboardButton('Vobkent')
        itembnt10=types.KeyboardButton('Qaravulbozor')
        itembnt10=types.KeyboardButton('Kogon sh')
        markup.add(itembnt1,itembnt2,itembnt3,itembnt4,itembnt5,itembnt6,itembnt7,itembnt8,itembnt9,itembnt10)

        msg = bot.send_message(chat_id, 'Tumanini tanlang', reply_markup=markup)
        bot.register_next_step_handler(msg, process_Tuman_step)
    except Exception as e:
        msg = bot.reply_to(message, 'Example:998997001670')
        bot.register_next_step_handler(msg, process_phone_step)



def process_Tuman_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.tuman = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(message.chat.id, 'Yashash manzilini kiriting ', reply_markup=markup)
    
        
        bot.register_next_step_handler(msg, process_manzil_step)

    except Exception as e:
       bot.reply_to(message, 'ooops!!')




def process_manzil_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.manzil = message.text
        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembnt1=types.KeyboardButton("O'quvchi")
        itembnt2=types.KeyboardButton('Talaba')
        itembnt3=types.KeyboardButton('Ishchi')
        itembnt4=types.KeyboardButton('Ishsiz')
        itembnt5=types.KeyboardButton('Nafaqada')
        markup.add(itembnt1,itembnt2,itembnt3,itembnt4,itembnt5)

        msg = bot.send_message(chat_id, "Ma'lumotingiz qanday??", reply_markup=markup)
        bot.register_next_step_handler(msg, process_malumot_step)
    except Exception as e:
        bot.reply_to(message, 'ooops!!')




def process_malumot_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.malumot = message.text
        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembnt1=types.KeyboardButton('Kompyuter savodxonligi')
        itembnt2=types.KeyboardButton('Kompyuter grafikasi')
        itembnt3=types.KeyboardButton('Web-dasturlash')
        itembnt4=types.KeyboardButton('Robototexnika')
        itembnt5=types.KeyboardButton('Mobil ilovalar yaratish')
        markup.add(itembnt1,itembnt2,itembnt3,itembnt4,itembnt5)

        msg = bot.send_message(chat_id, 'Qaysi kursga bormoqchisiz', reply_markup=markup)
        bot.register_next_step_handler(msg, process_soha_step)
    except Exception as e:
        bot.reply_to(message, 'ooops!!')



def process_soha_step(message):
    
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.soha = message.text

       
    bot.send_message(chat_id, getRegData(user, 'tg name', message.from_user.first_name), parse_mode="Markdown")
        
    bot.send_message('-1001164570771', getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")
    markup = types.ReplyKeyboardRemove(selective=False)

    msg = bot.send_message(chat_id, "Tabriklaymiz muvaffaqiyat registratsiyadan o'tingiz.\n Biz tez orada siz bilan bog'lanamiz\nAbout - /About\nRegistartiya - /Registartiya\nYordam - /help", reply_markup=markup)


    
def getRegData(user, title, name):
    t = Template('$title *$name* \n  FIO: *$FIO*\n Yosh: *$yosh* \n Raqam: *$phone* \n tuman: *$tuman* \n Yashash manzil: *$manzil* \n Malumoti: *$malumot* \n Tanlagan sohasi: *$soha*')

    return t.substitute({
        'title': title,
        'name': name,
        
        'FIO':user.FIO,
        'yosh': user.yosh,
        'phone': user.phone,
        'tuman': user.tuman,
        'manzil': user.manzil,
        'malumot': user.malumot,
        'soha': user.soha,
        
    })





@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'About - /About\nRegistartiya - /Registartiya\nYordam - /help')




@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'Itimos yozing')



bot.polling(none_stop=True)
    