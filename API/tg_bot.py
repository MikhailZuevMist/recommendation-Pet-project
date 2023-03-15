import telebot
from DataBase.Settings import bot_token, tg_admin_id

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     f'Hello {message.from_user.full_name}! I am recommendation system that can give you an advice what to wach or what to play based on your prefrences.')


# запускаем бота этой командой:

@bot.message_handler(regexp='Я в консоли')
def print_me(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Меню')
    markup.add(btn1)
    print(message.from_user.to_dict())
    text = f'Ты: {message.from_user.to_dict()}'
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.from_user.id == tg_admin_id and message.text == "Админка")
def admin_panel(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Общий баланс')
    btn2 = telebot.types.KeyboardButton('Все юзеры')
    btn3 = telebot.types.KeyboardButton('Данные по юзеру')
    btn4 = telebot.types.KeyboardButton('Удалить юзера')
    markup.add(btn1, btn2, btn3, btn4)
    text = f'Админ-панель'
    bot.send_message(message.chat.id, text, reply_markup=markup)





bot.infinity_polling()