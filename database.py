import psycopg
from datetime import datetime, timedelta
import schedule
import time
import app.dateandtimes as day
import logging
import app.slovo as sl



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

	#Функция для записи регистрирующихся клиентов в Базу данных
	@staticmethod
	def db_user_add(client_name, client_surname, client_tg_id, client_number_phone):
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				sql = 'INSERT INTO clients(client_name, client_surname, client_tg_id, client_number_phone) VALUES (%s, %s, %s, %s)'
				cursor.execute(sql, (client_name, client_surname, client_tg_id, client_number_phone))
				print("Запись выплнена")
		except Exception as _ex:
			print(f'[INFO] Ошибка при выполнении регистрации:', _ex)

	
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
							client_id varchar(30),
							procedure varchar(120)							
							)'''
				cursor.execute(sql1)
				logging.info(f'Таблица tab_ успешно создана')
		except Exception as create_e:
			print(f'Ошибка при создании или заполнении таблицы: {create_e}')


	#Метод заполняет таблицу временем. Запись производится с интервалом 30 минут, так же строки record заполняются нулями	
	@staticmethod
	def complection_new_table():
		start_time = datetime.strptime("10:00", "%H:%M")
		end_time = datetime.strptime("21:30", "%H:%M")
		current_time = start_time
		table_name = day.fifth_day.strftime("%d_%m")
		num_empty = 0
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				while current_time <= end_time:
					insert_query = f'INSERT INTO tab_{table_name} (recorder_time, record) VALUES (%s, %s) ON CONFLICT (recorder_time) DO NOTHING;'
					cursor.execute(insert_query, (current_time.strftime("%H:%M"), num_empty,))
					current_time += timedelta(minutes=30)
					logging.info(f'[INFO] запись {current_time} выполнена')
		except Exception as create_e:
				print(f'Ошибка при создании или заполнении таблицы: {create_e}')

	#При внесении изменений при регистрации строка с ранее внесенными данными полностью удаляется
	@staticmethod
	def delete_incorrect_data(old_id):
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				sql2 = 'DELETE FROM clients WHERE client_tg_id = %s'
				cursor.execute(sql2, (old_id,))
		except Exception as _ex:
			print(f'[INFO] Ошибка при выполнении удаления неверно внесенных данных:', _ex)		
		

	#Расписание для создания новой таблици для записи
	@staticmethod
	def schedule_table_creation():
		schedule.every().day.at('14:57').do(DbMarina.create_daily_table)
		schedule.every().day.at('14:58').do(DbMarina.complection_new_table)
		print('Планировщик запущен. Ожидание времени выполнения задачи...')
		while True:
			schedule.run_pending()
			time.sleep(1)


	#Создание таблици необходимой для регистрации клиентов
	@staticmethod
	def clietns():
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				sql1 = f'''CREATE TABLE IF NOT EXISTS clients
								(
								client_id serial,
								client_name varchar(20),
								client_surname varchar(20),
								client_tg_id varchar(50),
								client_number_phone varchar(20)							
								)'''
				cursor.execute(sql1)
				logging.info(f'Таблица tab_ успешно создана')
		except Exception as create_e:
			print(f'Ошибка при создании или заполнении таблицы: {create_e}')



	#Функция для записи клиентов на определенное время
	@staticmethod
	def db_schedule_add(recorder_time, procedure, client_id, date, record = 1):
		print(recorder_time, type(recorder_time))
		table_name = date
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				if procedure in sl.list_procedure_time_30min:
					sql = f'UPDATE tab_{table_name} SET record = %s, client_id = %s, procedure = %s WHERE recorder_time = %s;'
					cursor.execute(sql, (record, client_id, procedure, recorder_time))
				elif procedure in sl.list_procedure_time_60min:
					for _ in range(2):
						sql = f'UPDATE tab_{table_name} SET record = %s, client_id = %s, procedure = %s WHERE recorder_time = %s;'
						cursor.execute(sql, (record, client_id, procedure, recorder_time))
						db_time = datetime.strptime(recorder_time, "%H:%M")+timedelta(minutes=30)
						print(db_time)
						recorder_time = str(db_time)
						print(recorder_time)
				elif procedure in sl.list_procedure_time_90min:
					for _ in range(3):
						sql = f'UPDATE tab_{table_name} SET record = %s, client_id = %s, procedure = %s WHERE recorder_time = %s;'
						cursor.execute(sql, (record, client_id, procedure, recorder_time))
						db_time = datetime.strptime(recorder_time, "%H:%M")+timedelta(minutes=30)
						print(db_time)
						recorder_time = str(db_time.strftime("%H:%M"))
						print(recorder_time)
				else:
					for _ in range(4):
						sql = f'UPDATE tab_{table_name} SET record = %s, client_id = %s, procedure = %s WHERE recorder_time = %s;'
						cursor.execute(sql, (record, client_id, procedure, recorder_time))
						db_time = datetime.strptime(recorder_time, "%H:%M")+timedelta(minutes=30)
						print(db_time)
						recorder_time = str(db_time.strftime("%H:%M"))
						print(recorder_time)

				print("Запись выполнена")
		except Exception as _ex:
			print(f'[INFO] Ошибка при выполнении регистрации:', _ex)


	#Возвращает список для заполнения актуальной клавиатуры отображающей свободное время

	@staticmethod
	def screan_schedule(date):
		start_time = datetime.strptime("10:00", "%H:%M")
		end_time = datetime.strptime("21:30", "%H:%M")
		current_time = start_time
		table_name = date
		free_time = dict()
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				while current_time <= end_time:	
					sql = f'select record from tab_{table_name} where recorder_time = %s'
					cursor.execute(sql, (current_time.time(),))
					row = cursor.fetchone()
					if row == (1,):
						free_time[str(current_time.strftime("%H:%M"))] = 1
					else:
						free_time[str(current_time.strftime("%H:%M"))] = 0
					current_time += timedelta(minutes=30)
			return free_time
		except Exception as _ex:
			print(f'[INFO] :', _ex)
		
	@staticmethod
	def search_for_an_existing(client_id):
		#client_id = str(client_id)
		#print(type(client_id))
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				table_name = day.second_day.strftime("%d_%m")
				for _ in range(6):
					sql = f'select recorder_time from tab_{table_name} where client_id = %s'
					cursor.execute(sql, (client_id,))
					result = cursor.fetchall()
					formatted_result = [(time.strftime('%H:%M')) for (time,) in result]

					sql1 = f'select procedure from tab_{table_name} where client_id = %s'
					cursor.execute(sql1, (client_id,))
					formatted_result1 = cursor.fetchall()
					result1 = [i[0] for i in formatted_result1]

					res = [day.second_day.strftime("%d_%m"), formatted_result[0], result1[0]]
					#if cursor.fetchone() is not 'Null':
			return res
		except Exception as _ex:
			print(f'[INFO] :', _ex)
#_______________________________________________________________________#

#x = DbMarina()
#x.create_daily_table()
#x.complection_new_table()
#t = str(307582652)
#x.delete_incorrect_data(t)
#print(x.screan_schedule('03_03'))
#x = DbMarina()
#print(x.search_for_an_existing(7901916608))


# Запрос создания таблицы clients

#x.clietns()