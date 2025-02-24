import psycopg
from datetime import datetime, timedelta
import schedule
import time
import app.datatime as day
import logging


def get_connection():
	connection = psycopg.connect(
		host = '127.0.0.1',
		user = 'postgres',
		password = 'desam248533',
		dbname='schedule')
	connection.autocommit = True
	return connection


class DbMarina:
	"""
	Содержит основные функции взаиможействия с БД
	"""
	now = day.now


	@staticmethod
	def db_user_add(client_name, client_surname, client_tg_id, client_number_phone):
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				sql = 'INSERT INTO clients(client_name, client_surname, client_tg_id, client_number_phone) VALUES (%s, %s, %s, %s)'
				cursor.execute(sql, (client_name, client_surname, client_tg_id, client_number_phone))
				print("Запись выплнена")
		except Exception as _ex:
			logging.info(f'[INFO] Ошибка при выполнении регистрации:', _ex)

	#Функция для создания новой таблици для записи клиентов
	@staticmethod
	def create_daily_table():
		table_name = day.six_day.strftime("%d_%m")
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				sql1 = f'''CREATE TABLE IF NOT EXISTS tab_{table_name}
							(
							recorder_time TIME primary key,
							record integer,
							client_id integer							
							)'''
				cursor.execute(sql1)
				logging.info(f'Таблица tab_ успешно создана')
		except Exception as create_e:
			print(f'Ошибка при создании или заполнении таблицы: {create_e}')


x = DbMarina()
x.create_daily_table()

	#Метод заполняет таблицу временем. Запись производится с интервалом 30 минут, так же строки record заполняются нулями
	# @staticmethod
	# def complection_new_table():
	# 	start_time = datetime.strptime("10:00", "%H:%M")
	# 	end_time = datetime.strptime("21:30", "%H:%M")
	# 	current_time = start_time
	# 	table_name = day.six_day.strftime("%d_%m")
	# 	num_empty = 0

	# 	try:
	# 		connection = get_connection()
	# 		with connection.cursor() as cursor:
	# 			while current_time <= end_time:
	# 				insert_query = f'INSERT INTO tab_{table_name} (recorder_time, record) VALUES (%s, %s) ON CONFLICT (recorder_time) DO NOTHING;'
	# 				cursor.execute(insert_query, (current_time.strftime("%H:%M"), num_empty,))
	# 				current_time += timedelta(minutes=30)
	# 				logging.info(f'[INFO] запись {current_time} выполнена')
	# 	except Exception as create_e:
	# 			print(f'Ошибка при создании или заполнении таблицы: {create_e}')

	
#Финкция таймера когда будет созвадваться новая таблица
	
		
		# while True:
		# 	now = datetime.now()
		# 	next_run = (now.replace(hour=15, minute=17, second=0, microsecond=0)+ timedelta(days=(now.hour>=23)))
		# 	sleep_time = (next_run - now).total_seconds()
		# 	print(f'Следующая таблица будет создана через {sleep_time} секунд')
		# 	await asyncio.sleep(sleep_time)

		# 	await asyncio.to_thread(DbMarina.create_daily_table())




# client_name = 'Павел'
# client_surname = "Ускова"
# client_tg_id = 333333
# client_number_phone = "7-4234-456-44-33"




# x.db_user_add(client_name, client_surname, client_tg_id, client_number_phone)
# x.create_daily_table()
# x.complection_new_table()
