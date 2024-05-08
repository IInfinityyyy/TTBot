import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('tag')
    
@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('ttbase.db')
    cur = conn.cursor()

    cur.execute('''
CREATE TABLE IF NOT EXISTS ttbase (
    f1 TEXT,
    f2 TEXT,
    f3 TEXT,
    f4 TEXT,
    f5 TEXT,
    f6 TEXT,
    f7 TEXT,
    f8 TEXT,
    f9 TEXT,
    f10 TEXT,
    f11 TEXT,
    f12 TEXT,
    f13 TEXT,
    f14 TEXT,
    f15 TEXT,
    f16 TEXT,
    f17 TEXT,
    f18 TEXT,
    f19 TEXT,
    f20 TEXT
)
''')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, я TimeTableBot сокращено TTBot, выберите команду /TimeTable что бы увидеть расписание или выберите команду /HomeWork что бы посмотреть домашнее задание')

@bot.message_handler(commands=['TimeTable'])
def timetable(message):
    markup = types.ReplyKeyboardMarkup()
    monday = types.KeyboardButton('Понедельник')
    thuesday = types.KeyboardButton('Четверг')
    markup.row(monday, thuesday)
    tuesday = types.KeyboardButton('Вторник')
    friday = types.KeyboardButton('Пятница')
    markup.row(tuesday, friday)
    wedday = types.KeyboardButton('Среда')
    satday = types.KeyboardButton('Суббота')
    back = types.KeyboardButton('Назад')
    markup.row(wedday, satday)
    markup.row(back)
    bot.send_message(message.chat.id, f'Выберите день недели', reply_markup=markup)
    bot.register_next_step_handler(message, sendtt)

def sendtt(message):
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
        bot.send_message(message.chat.id, 'Хихи, а посхалки уже нет :^)')
    elif message.text == 'Назад':
        bot.register_next_step_handler(message, start)
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю, пожалуйста выберите день недели')
    bot.register_next_step_handler(message, sendtt)

@bot.message_handler(commands=['HomeWork'])
def homework(message):
    conn = sqlite3.connect('ttbase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ttbase')
    rows = cursor.fetchall()
    conn.close()

    markup = types.ReplyKeyboardMarkup()

    algebra = types.KeyboardButton('Алгебра')
    english = types.KeyboardButton('Английский язык')
    biology = types.KeyboardButton('Биология')
    edu_h = types.KeyboardButton('Восп. час')
    edu = types.KeyboardButton('Воспитание')
    wwhistory = types.KeyboardButton('Всемирная история')
    geography = types.KeyboardButton('География')
    geometry = types.KeyboardButton('Геометрия')
    informatics = types.KeyboardButton('Информатика')
    uzhistory = types.KeyboardButton('История Узбекистана')
    liter = types.KeyboardButton('Литература')
    pravo = types.KeyboardButton('Право')
    russ = types.KeyboardButton('Русский язык')
    tech = types.KeyboardButton('Технология')
    uzb = types.KeyboardButton('Узбекский язык')
    physic = types.KeyboardButton('Физика')
    fizra = types.KeyboardButton('Физкультура')
    himiya = types.KeyboardButton('Химия')
    cher = types.KeyboardButton('Черчение')
    economy = types.KeyboardButton('Экономика')
    bot.send_message(message.chat.id, f'Выберите предмет', reply_markup=markup)

    for row in rows:
        if message.text == 'Алгебра':
            print(row[0])

    
bot.infinity_polling()
