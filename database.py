import psycopg
from datetime import datetime, timedelta
import schedule
import time
import app.datatime as day




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
				sql ='''INSERT INTO clients(client_name, client_surname, client_tg_id, client_number_phone) VALUES (%s, %s, %s, %s)'''
				cursor.execute(sql, (client_name, client_surname, client_tg_id, client_number_phone))
				print("Запись выплнена")
		except Exception as _ex:
			print(f'[INFO] Ошибка при выполнении регистрации:', _ex)

	#Функция для создания новой таблици для записи клиентов
	@staticmethod
	def create_daily_table():
		today = day.now().strftime("%Y_%m_%d")
		table_name = day.six_day
		
		try:
			connection = get_connection()
			with connection.cursor as cursor:
				sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (
					record_time TIME PRIMARY KEY,
					client_name VARCHAR(255));'''
				cursor.execute(sql)
				connection.commit()
				print(f'Таблица {table_name} успешно создана')

				start_time = datetime.strptime("10:00", "%H:%M")
				end_time = datetime.strptime("21:30", "%H:%M")
				current_time = start_time

			# while current_time <= end_time:
			# 	insert_query = f"""
			# 	INSERT INTO {table_name} (record_time, client_name)
			# 	VALUES (%s, %s)
			# 	ON CONFLICT (record_time) DO NOTHING;
			# 	"""
			# 	cursor.execute(insert_query, (current_time.strftime("%H:%M"), None))
			# 	current_time += timedelta(minutes=30)

			connection.commit()
			print(f'Таблица {table_name} успешно заполнена временными интервалами')	
		except Exception as create_e:
			print(f'Ошибка при создании или заполнении таблицы: {create_e}')


	# @staticmethod
	# def run_sheduler():
	# 	schedule.every().day.at('14:42').do(create_daliy_table())
	# 	print('Планировщик запущен. Ожидание времени выполнения задачи...')
	# 	while True:
	# 		schedule.run_pending()
	# 		time.sleep(1)


#_______________________________________________________________________#

# import psycopg
# import schedule
# import time


# def get_connection():
# 	connection = psycopg.connect(
# 		host = '127.0.0.1',
# 		user = 'postgres',
# 		password = 'desam248533',
# 		dbname='schedule')
# 	connection.autocommit = True
# 	return connection

# class DbMarina:
# 	"""
# 	Содержит основные функции взаиможействия с БД
# 	"""
	

# 	@staticmethod
# 	def db_user_add(client_name, client_surname, client_tg_id, client_number_phone):
# 		try:
# 			connection = get_connection()
# 			with connection.cursor() as cursor:
# 				sql ='''INSERT INTO clients(client_name, client_surname, client_tg_id, client_number_phone) VALUES (%s, %s, %s, %s)'''
# 				cursor.execute(sql, (client_name, client_surname, client_tg_id, client_number_phone))
# 				print("Запись выплнена")
# 		except Exception as _ex:
# 			print(f'[INFO] Ошибка при выполнении регистрации:', _ex)


#         #sql_inser = '''INSERT INTO clients(client_id, client_name, client_surname, client_tg_id, client_number_phone) 
# 		#SELECT row_number() OVER (ORDER BY client_id) + 1, %s, %s, %s, %s FROM clients'''



# 	@staticmethod
# 	def create_daily_table():
# 		today = day.now().strftime("%Y_%m_%d")
# 		table_name = day.six_day
		
# 		try:
# 			connection = get_connection()
# 			with connection.cursor as cursor:
# 				sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (
# 					record_time TIME PRIMARY KEY,
# 					client_name VARCHAR(255));'''
# 				cursor.execute(sql)
# 				connection.commit()
# 				print(f'Таблица {table_name} успешно создана')

# 				start_time = datetime.strptime("10:00", "%H:%M")
# 				end_time = datetime.strptime("21:30", "%H:%M")
# 				current_time = start_time

# 			# while current_time <= end_time:
# 			# 	insert_query = f"""
# 			# 	INSERT INTO {table_name} (record_time, client_name)
# 			# 	VALUES (%s, %s)
# 			# 	ON CONFLICT (record_time) DO NOTHING;
# 			# 	"""
# 			# 	cursor.execute(insert_query, (current_time.strftime("%H:%M"), None))
# 			# 	current_time += timedelta(minutes=30)

# 			connection.commit()
# 			print(f'Таблица {table_name} успешно заполнена временными интервалами')	
# 		except Exception as create_e:
# 			print(f'Ошибка при создании или заполнении таблицы: {create_e}')
