from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Овен'),
            KeyboardButton(text='Телец'),
        ], [
            KeyboardButton(text='Близнецы'),
            KeyboardButton(text='Рак'),
        ], [
            KeyboardButton(text='Лев'),
            KeyboardButton(text='Дева'),
        ], [
            KeyboardButton(text='Весы'),
            KeyboardButton(text='Скорпион'),
        ], [
            KeyboardButton(text='Стрелец'),
            KeyboardButton(text='Козерог'),
        ], [
            KeyboardButton(text='Водолей'),
            KeyboardButton(text='Рыбы'),
        ]
    ]
)
