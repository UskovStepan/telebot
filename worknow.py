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
# 		password = 'desam248533',
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

# x = DbMarina()
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
		

# x = DbMarina()
# resutl = x.screan_schedule('03_03')