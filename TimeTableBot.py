import telebot
from telebot import types


bot = telebot.TeleBot('Здесь должен быть код тг бота ;) ')
    
    
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    monday = types.KeyboardButton('Понедельник')
    thuesday = types.KeyboardButton('Четверг')
    markup.row(monday, thuesday)
    tuesday = types.KeyboardButton('Вторник')
    friday = types.KeyboardButton('Пятница')
    markup.row(tuesday, friday)
    wedday = types.KeyboardButton('Среда')
    satday = types.KeyboardButton('Суббота')
    markup.row(wedday, satday)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, я TimeTableBot сокращено TTBot, что-бы увидеть расписание выберите день недели', reply_markup=markup)

@bot.message_handler()
def tt(message):
    if message.text == 'Понедельник':
        bot.send_message(message.chat.id, f'\nРасписание на понедельник: \n1) <b>Информатика</b> | <b>Узбекский язык</b> 8:30 - 9:10 \n2) <b>Узбекский язык</b> | <b>Информатика</b> 9:15 - 9:55 \n3) <b>Алгебра</b> 10:05 - 10:45 \n4) <b>Химия</b> 11:00 - 11:40 \n5) <b>Русский язык</b> 11:45 - 12:25', parse_mode='html')
    elif message.text == 'Вторник':
        bot.send_message(message.chat.id, f'\nРасписание на вторник: \n1) <b>Геометрия</b> 8:30 - 9:10 \n2) <b>География</b> 9:15 - 9:55 \n3) <b>Литература</b> 10:05 - 10:45 \n4) <b>Физика</b> 11:00 - 11:40 \n5) <b>Физ-ра</b> 11:45 - 12:25 \n6) <b>Английский язык</b> 12:30 - 13:10', parse_mode='html')
    elif message.text == 'Среда':
        bot.send_message(message.chat.id, f'\nРасписание на cреду: \n1) <b>Русский язык</b> 8:30 - 9:10 \n2) <b>Алгебра</b> 9:15 - 9:55 \n3) <b>Биология</b> 10:05 - 10:45 \n4) <b>Экономика</b> 11:00 - 11:40 \n5) <b>Узбекский язык</b> 11:45 - 12:25 \n6) <b>Технология</b> 12:30 - 13:10', parse_mode='html')
    elif message.text == 'Четверг':
        bot.send_message(message.chat.id, f'\nРасписание на четверг: \n1) <b>Английский язык</b> 8:30 - 9:10 \n2) <b>Литература</b> 9:15 - 9:55 \n3) <b>Алгебра</b> 10:05 - 10:45 \n4) <b>История Узб.</b> 11:00 - 11:40 \n5) <b>Химия</b> 11:45 - 12:25 \n6) <b>Физ-ра</b> 12:30 - 13:10', parse_mode='html')
    elif message.text == 'Пятница':
        bot.send_message(message.chat.id, f'\nРасписание на пятницу: \n1) <b>Восп. час</b> 8:30 - 9:10 \n2) <b>Узбекский язык</b> 9:15 - 9:55 \n3) <b>Геометрия</b> 10:05 - 10:45 \n4) <b>Всемирная история</b> 11:00 - 11:40 \n5) <b>Биология</b> 11:45 - 12:25 \n6) <b>Воспитание</b> 12:30 - 13:10', parse_mode='html')
    elif message.text == 'Суббота':
        bot.send_message(message.chat.id, f'\nРасписание на субботу: \n1) <b>Черчение</b> 8:30 - 9:10 \n2) <b>Физика</b> 9:15 - 9:55 \n3) <b>История Узб.</b> 10:05 - 10:45 \n4) <b>Английский язык</b> 11:00 - 11:40 \n5) <b>Право</b> 11:45 - 12:25', parse_mode='html')
    elif message.text == 'Воскресенье':
        bot.send_message(message.chat.id, 'Ты дурак?')
        bot.send_message(message.chat.id, 'Кто учится в воскресенье?')
        bot.send_message(message.chat.id, '-_-')
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю, пожалуйста выберите день недели')
    
    
bot.infinity_polling()
