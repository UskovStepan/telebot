import asyncio
import logging
import database as db

from aiogram import Bot, Dispatcher
from config import TOKEN
from app.hendlers import router
from datetime import datetime, timedelta
import schedule
import time



bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
	dp.include_router(router)	
	await dp.start_polling(bot)
	#asyncio.create_task(schedule_table_creation())

#Финкция таймера когда будет созвадваться новая таблица
# async def schedule_table_creation():
# 	schedule.every().day.at('15:22').do(db.DbMarina.create_daily_table)
# 	print('Планировщик запущен. Ожидание времени выполнения задачи...')
# 	while True:
# 		schedule.run_pending()
# 		time.sleep(1)


	# while True:
	# 	now = datetime.now()
	# 	next_run = (now.replace(hour=15, minute=17, second=0, microsecond=0)+ timedelta(days=(now.hour>=23)))
	# 	sleep_time = (next_run - now).total_seconds()
	# 	print(f'Следующая таблица будет создана через {sleep_time} секунд')
	# 	await asyncio.sleep(sleep_time)

	# 	await asyncio.to_thread(db.DbMarina.create_daily_table())
		
		


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	asyncio.run(main())
	