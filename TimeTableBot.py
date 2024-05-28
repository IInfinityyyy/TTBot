from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///homework.db'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Homework(Base):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True)
    subject = Column(String, unique=True, nullable=False)
    homework = Column(Text, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#! Бот может отвечать в группе без доступа с сообщениям

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import logging

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# *Стартовая клавиатура
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton('Увидеть школьное расписание'))
main_keyboard.add(KeyboardButton('Увидеть домашнии задания'))

# *Клавиатура с предметами
subjects_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
subjects = ['Алгебра', 'Английский_язык', 'Биология', 'Воспит_час', 'Воспитание',
            'Всемирная_история', 'География', 'Геометрия', 'Информатика',
            'История_Узбекистана', 'Литература', 'Право', 'Русский_язык',
            'Технология', 'Узбекский_язык', 'Физика', 'Физкультура', 'Химия',
            'Черчение', 'Экономика']
for i in range(0, len(subjects), 1):  # *Разбиваем на строки по 3 кнопки
    subjects_keyboard.row(*[types.KeyboardButton(subject) for subject in subjects[i:i+1]])

# *Обработчик команду start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет я твой помощник по школе <b>TimeTableBot</b>, и помогу тебе узнавать расписание уроков и домашнии задания. Выбери действие:", reply_markup=main_keyboard, parse_mode='html')

# *Школьное расписание
@dp.message_handler(lambda message: message.text == "Увидеть школьное расписание")
async def show_schedule(message: types.Message):
    await message.reply("""
\nРасписание на <b>Понедельник</b>: \n1) <b>Информатика</b> | <b>Узбекский язык</b> 8:30 - 9:10 \n2) <b>Узбекский язык</b> | <b>Информатика</b> 9:15 - 9:55 \n3) <b>Алгебра</b> 10:05 - 10:45 \n4) <b>Химия</b> 11:00 - 11:40 \n5) <b>Русский язык</b> 11:45 - 12:25
\nРасписание на <b>Вторник</b>: \n1) <b>Геометрия</b> 8:30 - 9:10 \n2) <b>География</b> 9:15 - 9:55 \n3) <b>Литература</b> 10:05 - 10:45 \n4) <b>Физика</b> 11:00 - 11:40 \n5) <b>Физ-ра</b> 11:45 - 12:25 \n6) <b>Английский язык</b> 12:30 - 13:10
\nРасписание на <b>Среду</b>: \n1) <b>Русский язык</b> 8:30 - 9:10 \n2) <b>Алгебра</b> 9:15 - 9:55 \n3) <b>Биология</b> 10:05 - 10:45 \n4) <b>Экономика</b> 11:00 - 11:40 \n5) <b>Узбекский язык</b> 11:45 - 12:25 \n6) <b>Технология</b> 12:30 - 13:10
\nРасписание на <b>Четверг</b>: \n1) <b>Английский язык</b> 8:30 - 9:10 \n2) <b>Литература</b> 9:15 - 9:55 \n3) <b>Алгебра</b> 10:05 - 10:45 \n4) <b>История Узб.</b> 11:00 - 11:40 \n5) <b>Химия</b> 11:45 - 12:25 \n6) <b>Физ-ра</b> 12:30 - 13:10
\nРасписание на <b>Пятницу</b>: \n1) <b>Восп. час</b> 8:30 - 9:10 \n2) <b>Узбекский язык</b> 9:15 - 9:55 \n3) <b>Геометрия</b> 10:05 - 10:45 \n4) <b>Всемирная история</b> 11:00 - 11:40 \n5) <b>Биология</b> 11:45 - 12:25 \n6) <b>Право</b> 12:30 - 13:10
\nРасписание на <b>Субботу</b>: \n1) <b>Черчение</b> 8:30 - 9:10 \n2) <b>Физика</b> 9:15 - 9:55 \n3) <b>История Узб.</b> 10:05 - 10:45 \n4) <b>Английский язык</b> 11:00 - 11:40 \n5) <b>Воспитание</b> 11:45 - 12:25

\np.s расписание можно закрепить что бы мне лишний раз его не отправлять 
""", parse_mode='html')

# *Выбор предмета
@dp.message_handler(lambda message: message.text == "Увидеть домашнии задания")
async def show_homework_options(message: types.Message):
    await message.reply("Выбери предмет по которому хочешь увидеть домашнее задание.\nЧто бы изменить домашнее задание отправь сообщение следующим образом: <b>/upd Предмет Новое задание</b>\nЕсли предмет состоит из двух слов то между ними должен стоять знак \"_\"", reply_markup=subjects_keyboard, parse_mode='html')

# *Отправка домашнего задания
@dp.message_handler(lambda message: message.text in ['Алгебра', 'Английский_язык', 'Биология', 'Воспит_час', 'Воспитание',
            'Всемирная_история', 'География', 'Геометрия', 'Информатика',
            'История_Узбекистана', 'Литература', 'Право', 'Русский_язык',
            'Технология', 'Узбекский_язык', 'Физика', 'Физкультура', 'Химия',
            'Черчение', 'Экономика'])
async def show_homework(message: types.Message):
    subject = message.text
    homework = session.query(Homework).filter_by(subject=subject).first()
    if homework:
        await message.reply(f"Домашнее задание по предмету {subject}: {homework.homework}")
    else:
        await message.reply(f"Домашнее задание по предмету {subject} отсутствует")

# *Функция изменения задания по предмету
@dp.message_handler(commands=['upd'])
async def update_homework(message: types.Message):
    try:
        _, subject, new_homework = message.text.split(' ', 2)
        homework = session.query(Homework).filter_by(subject=subject).first()
        if homework:
            homework.homework = new_homework
        else:
            homework = Homework(subject=subject, homework=new_homework)
            session.add(homework)
        session.commit()
        await message.reply(f"Домашнее задание по предмету {subject} обновлено")
    except ValueError:
        await message.reply("Напоминаю, для изменение домашнего задания отправь сообщение таким образом: <b>/upd Предмет Новое задание</b>")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
# !Расширение Better Commands для пророботанных комментариев
