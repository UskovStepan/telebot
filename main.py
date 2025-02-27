import asyncio
import logging
# import database as db

from aiogram import Bot, Dispatcher
from config import TOKEN
from app.hendlers import router

# import schedule
# import time



bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
	dp.include_router(router)
	await dp.start_polling(bot)
      
		

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	asyncio.run(main())
	