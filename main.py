import telebot
import random

from env import token

bot = telebot.TeleBot(token)

Keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
Keyboard.add(button1, button2)
@bot.message_handler(commands=['start','hi'])
def starts_fucsion(message):
    msg=bot.send_message(message.chat.id,f'Привет {message.chat.first_name} начнем игру?', reply_markup=Keyboard)
    bot.register_next_step_handler(msg,answer_check)
#     bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAJKSGOhPZhKwcBvDX_tvRPCUVdP5jR8AAKKAAOPFmk0PxXa0k_jQFQsBA')
#     bot.send_photo(message.chat.id,'https://miro.medium.com/max/1400/1*m0H6-tUbW6grMlezlb52yw.png')


def answer_check(msg):
    if msg.text == 'Да':
        bot.send_message(msg.chat.id,'у тебя есть 3 попытки угодать число от 1 до 10')
        random_number = random.randint(1,10)
        p = 3
        start_game(msg, random_number, p)
    else:
        bot.send_message(msg.chat.id,'иди гуляй!')


def start_game(msg, random_number, p):
    msg = bot.send_message(msg.chat.id,'Введи чилсоот 1 до 10: ')
    bot.register_next_step_handler(msg, chack_func, random_number, p-1)


def chack_func(msg, random_number, p):
    if msg.text == str(random_number):
        bot.send_message(msg.chat,id, 'Вы победили!')

    elif p == 0:
        bot.send_message(msg.chat.id, f'Вы проиграли! Число было -{random_number}')
    else:
        bot.send_message(msg.chat.id, f'Попробуй еще раз у тебя осталось {p} попыток')
        start_game(msg, random_number, p)



# @bot.message_handler()
# def ech_all(message):
#     bot.send_message(message.chat.id,message.text)

bot.polling()


#git init
#git remote add origin ssh/https

#git add.
#git commit -m 'names commit'
#git push oringin master 