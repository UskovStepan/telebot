# import psycopg
# from datetime import datetime, timedelta
# import schedule
# import time
# import app.dateandtimes as day
# import logging
# import app.slovo as sl


# def get_connection():
# 	connection = psycopg.connect(
# 		host = '127.0.0.1',
# 		user = 'postgres',
# 		password = '248533',
# 		dbname='schedule')
# 	connection.autocommit = True
# 	return connection



                   
           

# class DbMarina:
# 	"""
# 	Содержит основные функции взаиможействия с БД
# 	"""
# 	now = day.now


# 	@staticmethod
# 	def create_daily_table():
# 		table_name = day.six_day.strftime("%d_%m")
# 		try:
# 			connection = get_connection()
# 			with connection.cursor() as cursor:
# 				sql1 = f'''CREATE TABLE IF NOT EXISTS tab_{table_name}
# 							(
# 							recorder_time TIME primary key,
# 							record integer,
# 							client_id varchar(30),
# 							procedure varchar(120)							
# 							)'''
# 				cursor.execute(sql1)
# 				logging.info(f'Таблица tab_ успешно создана')
# 		except Exception as create_e:
# 			print(f'Ошибка при создании или заполнении таблицы: {create_e}')

# 	@staticmethod
# 	def complection_new_table():
# 		start_time = datetime.strptime("10:00", "%H:%M")
# 		end_time = datetime.strptime("21:30", "%H:%M")
# 		current_time = start_time
# 		table_name = day.six_day.strftime("%d_%m")
# 		num_empty = 0
# 		try:
# 			connection = get_connection()
# 			with connection.cursor() as cursor:
# 				while current_time <= end_time:
# 					insert_query = f'INSERT INTO tab_{table_name} (recorder_time, record) VALUES (%s, %s) ON CONFLICT (recorder_time) DO NOTHING;'
# 					cursor.execute(insert_query, (current_time.strftime("%H:%M"), num_empty,))
# 					current_time += timedelta(minutes=30)
# 					logging.info(f'[INFO] запись {current_time} выполнена')
# 		except Exception as create_e:
# 				print(f'Ошибка при создании или заполнении таблицы: {create_e}')


# 	@staticmethod
# 	def clients():
# 		try:
# 			connection = get_connection()
# 			with connection.cursor() as cursor:
# 				sql1 = f'''CREATE TABLE IF NOT EXISTS clients
# 								(
# 								client_id serial,
# 								client_name varchar(20),
# 								client_surname varchar(20),
# 								client_tg_id varchar(50),
# 								client_number_phone varchar(20),
# 								client_ban integer							
# 								)'''
# 				cursor.execute(sql1)
# 				logging.info(f'Таблица tab_ успешно создана')
# 		except Exception as create_e:
# 			print(f'Ошибка при создании или заполнении таблицы: {create_e}')


# x = DbMarina()
# x.clients()
# x.create_daily_table()
# x.complection_new_table()


# 	@staticmethod
# 	def screan_schedule(date):
# 		start_time = datetime.strptime("10:00", "%H:%M")
# 		end_time = datetime.strptime("21:30", "%H:%M")
# 		current_time = start_time
# 		table_name = date
# 		free_time = dict()
# 		try:
# 			connection = get_connection()
# 			with connection.cursor() as cursor:
# 				while current_time <= end_time:	
# 					sql = f'select record from tab_{table_name} where recorder_time = %s'
# 					cursor.execute(sql, (current_time.time(),))
# 					row = cursor.fetchone()
# 					print(current_time.time(), type(row))
# 					if row == (1,):
# 						free_time[str(current_time.time())] = 1
# 					else:
# 						free_time[str(current_time.time())] = 0
# 					current_time += timedelta(minutes=30)
# 			return free_time
# 		except Exception as _ex:
# 			print(f'[INFO] :', _ex)
# 


#	
# 	@staticmethod
# 	def screan_schedule(date):
# 		start_time = datetime.strptime("10:00", "%H:%M")
# 		end_time = datetime.strptime("21:30", "%H:%M")
# 		current_time = start_time
# 		table_name = date
# 		free_time = dict()
# 		try:
# 			connection = get_connection()
# 			with connection.cursor() as cursor:
# 				while current_time <= end_time:	
# 					sql = f'select record from tab_{table_name} where recorder_time = %s'
# 					cursor.execute(sql, (current_time.time(),))
# 					row = cursor.fetchone()
# 					if row == (1,):
# 						free_time[str(current_time.strftime("%H:%M"))] = 1
# 					else:
# 						free_time[str(current_time.strftime("%H:%M"))] = 0
# 					current_time += timedelta(minutes=30)
# 			return free_time
# 		except Exception as _ex:
# 			print(f'[INFO] :', _ex)


# 	@staticmethod
# 	def check_available_slots(procedure, date):
# 		table_name = date
# 		start_time = datetime.strptime("10:00", "%H:%M")
# 		end_time = datetime.strptime("21:30", "%H:%M")
# 		current_time = start_time
# 		free_time = DbMarina.screan_schedule(table_name)
# 		result = {}
# 		try:
# 			if procedure in sl.list_procedure_time_30min:
# 				result = free_time
# 			elif procedure in sl.list_procedure_time_60min:
# 				while current_time <= end_time:	
# 					for i in range(23):
# 						if free_time[sl.times[i]]+free_time[sl.times[i+1]] == 0:
# 							result[sl.times[i]] = 0
# 							current_time += timedelta(minutes=30)
# 						else:
# 							result[sl.times[i]] = 1
# 							current_time += timedelta(minutes=30)
				
# 			elif procedure in sl.list_procedure_time_90min:
# 				while current_time <= end_time:
# 					for i in range(22):
# 						if free_time[sl.times[i]] + free_time[sl.times[i+1]] + free_time[sl.times[i+2]] == 0:
# 							result[sl.times[i]] = 0
# 							current_time += timedelta(minutes=30)
# 						else:
# 							result[sl.times[i]] = 1
# 							current_time += timedelta(minutes=30)
# 			elif procedure in sl.list_procedure_time_120min:
# 				while current_time <= end_time:
# 					for i in range(21):
# 						if free_time[sl.times[i]] + free_time[sl.times[i+1]] + free_time[sl.times[i+2]] + free_time[sl.times[i+3]] == 0:
# 							result[sl.times[i]] = 0
# 							current_time += timedelta(minutes=30)
# 						else:
# 							result[sl.times[i]] = 1
# 							current_time += timedelta(minutes=30)
# 			print(result)
# 			return result

# 		except Exception as _ex:
# 			print(f'[INFO] :', _ex)
					

# x = DbMarina()
# #resutl = x.db_schedule_add('10:00', 'Мужская стрижка', '666666', '05_03')
# x.check_available_slots('Рекавери+Детокс+Стрижка', '08_03')
