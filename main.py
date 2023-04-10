import asyncio
from config import TOKEN, URL
from aiogram import Bot, Dispatcher, executor


TOKEN = TOKEN

loop = asyncio.new_event_loop()
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=bot)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
