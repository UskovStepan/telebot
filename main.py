import os
import asyncio
import logging


from aiogram import Bot, Dispatcher
from config import TOKEN
from app.hendlers import router
#from dotenv import load_dotenv
# import schedule
# import time





async def main():
	#load_dotenv()
	bot = Bot(token=TOKEN)
	dp = Dispatcher()
	dp.include_router(router)
	await dp.start_polling(bot)
      
		

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	asyncio.run(main())
	