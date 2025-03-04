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
	
	
	#Функция проверки регистрации
	@staticmethod
	def check_user_bd(client_id):
		result = dict()
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				sql = 'SELECT * from clients where client_tg_id = %s'
				cursor.execute(sql, (str(client_id),))
				res = cursor.fetchall()
				if len(res)>0:
					result['id'] = res[0][0]
					result['name'] = res[0][1]
					result['surname'] = res[0][2]
					result['tg_id'] = res[0][3]
					result['number_phone'] = res[0][4]
			if result == {}:
				result = None
		except Exception as _ex:
			print(f'[INFO] Ошибка при выполнении регистрации:', _ex)
		return result
	
	#Функция для создания новой таблици для записи клиентов
	@staticmethod
	def create_daily_table():
		table_name = day.now.strftime("%d_%m")
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
		table_name = day.now.strftime("%d_%m")
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
						recorder_time = str(db_time)
				elif procedure in sl.list_procedure_time_90min:
					for _ in range(3):
						sql = f'UPDATE tab_{table_name} SET record = %s, client_id = %s, procedure = %s WHERE recorder_time = %s;'
						cursor.execute(sql, (record, client_id, procedure, recorder_time))
						db_time = datetime.strptime(recorder_time, "%H:%M")+timedelta(minutes=30)
						recorder_time = str(db_time.strftime("%H:%M"))	
				else:
					for _ in range(4):
						sql = f'UPDATE tab_{table_name} SET record = %s, client_id = %s, procedure = %s WHERE recorder_time = %s;'
						cursor.execute(sql, (record, client_id, procedure, recorder_time))
						db_time = datetime.strptime(recorder_time, "%H:%M")+timedelta(minutes=30)
						recorder_time = str(db_time.strftime("%H:%M"))

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
	#Функция для проверки свободного времени в зависимости от времени выполнения процедуры

	@staticmethod
	def check_available_slots(procedure, date):
		table_name = date
		start_time = datetime.strptime("10:00", "%H:%M")
		end_time = datetime.strptime("21:30", "%H:%M")
		current_time = start_time
		free_time = DbMarina.screan_schedule(table_name)
		result = {}
		try:
			if procedure in sl.list_procedure_time_30min:
				result = free_time
			elif procedure in sl.list_procedure_time_60min:
				while current_time <= end_time:	
					for i in range(23):
						if free_time[sl.times[i]]+free_time[sl.times[i+1]] == 0:
							result[sl.times[i]] = 0
							current_time += timedelta(minutes=30)
						else:
							result[sl.times[i]] = 1
							current_time += timedelta(minutes=30)
				
			elif procedure in sl.list_procedure_time_90min:
				while current_time <= end_time:
					for i in range(22):
						if free_time[sl.times[i]] + free_time[sl.times[i+1]] + free_time[sl.times[i+2]] == 0:
							result[sl.times[i]] = 0
							current_time += timedelta(minutes=30)
						else:
							result[sl.times[i]] = 1
							current_time += timedelta(minutes=30)
			elif procedure in sl.list_procedure_time_120min:
				while current_time <= end_time:
					for i in range(21):
						if free_time[sl.times[i]] + free_time[sl.times[i+1]] + free_time[sl.times[i+2]] + free_time[sl.times[i+3]] == 0:
							result[sl.times[i]] = 0
							current_time += timedelta(minutes=30)
						else:
							result[sl.times[i]] = 1
							current_time += timedelta(minutes=30)
			return result
		
		except Exception as _ex:
			print(f'[INFO] :', _ex)
					
		 

	#Функция проверяет существует ли запись в БД		
	@staticmethod
	def search_for_an_existing(client_id):
		#client_id = str(client_id)
		print(client_id)
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				current_data = day.now
				res = dict()
				for _ in range(5):
					table_name = current_data.strftime('%d_%m')
					sql = f'select recorder_time, procedure from tab_{table_name} where client_id = %s'
					cursor.execute(sql, (str(client_id),))
					result = cursor.fetchall()
					if len(result)>0:
						res['date_rec'] = table_name
						res['recorder_time'] = result[0][0].strftime('%H:%M')  
						res['procedure'] = result[0][1]
						break
					else:
						current_data += timedelta(days=1)
			if res == {}:
				res = None		
					#res = [day.now.strftime("%d_%m"), formatted_result[0], result1[0]]
					#if cursor.fetchone() is not 'Null':
			return res
		except Exception as _ex:
			print(f'[INFO] :', _ex)
			return None
		


	#Функция проверяет Зарегистрирован ли пользователь, прежде чем записаться		
	@staticmethod
	def search_registr(client_id):
		
		flag = False
		try:
			connection = get_connection()
			with connection.cursor() as cursor:
				sql2 = 'SELECT * FROM clients WHERE client_tg_id = %s'
				cursor.execute(sql2, (str(client_id),))
				result = cursor.fetchall()
				if len(result) > 0:
					flag = True
			return flag
		except Exception as _ex:
			print(f'[INFO] Ошибка при выполнении удаления неверно внесенных данных:', _ex)	


#____________________________________________________________________#


	
#_______________________________________________________________________#
	


#x = DbMarina()

#x.search_registr('6791852890')


#x.check_available_slots('Рекавери+Детокс+Стрижка', '05_03')
#x.generate_time_slots()

#t = str(307582652)
#x.delete_incorrect_data(t)
#print(x.screan_schedule('05_03'))

#print(x.search_for_an_existing('870857305'))
#print(x.check_user_bd('30758265'))


# Запрос создания таблицы clients

#x.clietns()