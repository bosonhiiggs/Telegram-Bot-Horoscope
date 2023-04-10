import requests
from bs4 import BeautifulSoup
from main import dp, bot
from aiogram.types import Message
from keyboards import keyboard
from aiogram.dispatcher.filters import Text


@dp.message_handler(commands=['start'])
async def welcome_message(message: Message):
    await message.answer('Я Гороскоп-бот. \nВыбери знак зодика', reply_markup=keyboard)


@dp.message_handler(Text(equals=['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион',
                                 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']))
async def zodiac_sing(message: Message):
    horo_dict = {
        'ОВЕН': None,
        'ТЕЛЕЦ': None,
        'БЛИЗНЕЦЫ': None,
        'РАК': None,
        'ЛЕВ': None,
        'ДЕВА': None,
        'ВЕСЫ': None,
        'СКОРПИОН': None,
        'СТРЕЛЕЦ': None,
        'КОЗЕРОГ': None,
        'ВОДОЛЕЙ': None,
        'РЫБЫ': None,
    }

    zodiac_sing = message.text
    req = requests.get('https://74.ru/horoscope/daily/')
    soup = BeautifulSoup(req.text, 'html.parser')

    all_horo_text = soup.findAll('div', class_='BDPZt KUbeq')

    count = 0
    for key, value in horo_dict.items():
        horo_dict[key] = all_horo_text[count].text
        count += 1

    # await message.answer(horo_dict[zodiac_sing.upper()])

    if zodiac_sing.upper() == 'ОВЕН':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/aries.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'ТЕЛЕЦ':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/taurus.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'БЛИЗНЕЦЫ':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/gemini.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'РАК':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/cancer.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'ЛЕВ':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/leo.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'ДЕВА':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/virgo.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'ВЕСЫ':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/libra.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'СКОРПИОН':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/scorpio.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'СТРЕЛЕЦ':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/sagittarius.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'КОЗЕРОГ':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/capricorn.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'ВОДОЛЕЙ':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/aquarius.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
    elif zodiac_sing.upper() == 'РЫБЫ':
        await bot.send_photo(chat_id=message.chat.id,
                             photo=open('zodiac-image/pisces.jpg', 'rb'),
                             caption=horo_dict[zodiac_sing.upper()])
