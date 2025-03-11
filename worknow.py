from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from aiogram.filters.callback_data import CallbackData

# Создаем экземпляр бота и диспетчера
bot = Bot(token="7901916608:AAEUmjTFjM9a0amlNnEtlY438FAn6y-lqko")
dp = Dispatcher()

# Создаем CallbackData для категорий и товаров
category_cb = CallbackData('category', 'id', 'name')
product_cb = CallbackData('product', 'id', 'category_id')

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    
    # Добавляем кнопки для категорий
    builder.row(
        types.InlineKeyboardButton(
            text="Category 1",
            callback_data=category_cb.new(id=1, name="Category 1")
        ),
        types.InlineKeyboardButton(
            text="Category 2",
            callback_data=category_cb.new(id=2, name="Category 2")
        )
    )
    
    await message.answer("Выберите категорию:", reply_markup=builder.as_markup())

# Обработчик callback-запросов для категорий
@dp.callback_query(category_cb.filter())
async def process_category(callback: CallbackQuery, callback_data: dict):
    category_id = callback_data['id']
    category_name = callback_data['name']
    
    builder = InlineKeyboardBuilder()
    
    # Добавляем кнопки для товаров в выбранной категории
    builder.row(
        types.InlineKeyboardButton(
            text="Product 1",
            callback_data=product_cb.new(id=1, category_id=category_id)
        ),
        types.InlineKeyboardButton(
            text="Product 2",
            callback_data=product_cb.new(id=2, category_id=category_id)
        )
    )
    
    await callback.message.edit_text(f"Вы выбрали категорию: {category_name}", reply_markup=builder.as_markup())

# Обработчик callback-запросов для товаров
@dp.callback_query(product_cb.filter())
async def process_product(callback: CallbackQuery, callback_data: dict):
    product_id = callback_data['id']
    category_id = callback_data['category_id']
    
    await callback.answer(f"Вы выбрали товар {product_id} в категории {category_id}")

# Запуск бота
if __name__ == "__main__":
    dp.run_polling(bot)
    
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
# 		table_name = day.fifth_day.strftime("%d_%m")
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
# 		table_name = day.fifth_day.strftime("%d_%m")
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
# x.clients()
# x.create_daily_table()
# x.complection_new_table()


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



	
# 	@staticmethod
# 	def admin_screan_schedule(date):
# 		start_time = datetime.strptime("10:00", "%H:%M")
# 		end_time = datetime.strptime("21:30", "%H:%M")
# 		current_time = start_time
# 		table_name = date
# 		spisok = []
# 		result = sl.admin_screan
# 		try:
# 			connection = get_connection()
# 			with connection.cursor() as cursor:
# 				while current_time <= end_time:	
# 					sql = f'select * from tab_{table_name} where recorder_time = %s'
# 					cursor.execute(sql, (str(current_time),))
# 					row = cursor.fetchone()
# 					cr_time = current_time
# 					if row[1] != 0:
# 						sql2 = f'SELECT * FROM clients where client_tg_id = %s'
# 						cursor.execute(sql2, (str(row[2]),))
# 						row2 = cursor.fetchone()
# 						spisok = [row2[1], row2[2], row[3], row2[4]]						
# 						result[cr_time.strftime("%H:%M")] = spisok
# 					else:
# 						result[cr_time.strftime("%H:%M")] = 'Свободно'
# 					current_time += timedelta(minutes=30)
# 			print(result)
# 			return result
# 		except Exception as _ex:
# 			print(f'[INFO] Ошибка при создании отчета о расписании на день для администратора', _ex)
	
# 	@staticmethod
# 	def read_admin_screan_schedule(date):
# 		formatted_text = ''
# 		x = DbMarina.admin_screan_schedule(date)
# 		print(x)
# 		for time_slot, status in x.items():
# 			if status == 'Свободно':
# 				formatted_text += f'{time_slot} - Свободно\n'
# 			elif isinstance(status, list):
# 				name, surname, procedure, phone = status
# 				formatted_text += f'{time_slot} - {name} {surname} проц. {procedure} тел: {phone}\n'
# 		print(formatted_text.strip())
# 		return formatted_text.strip()

			

#x = DbMarina()

# #resutl = x.db_schedule_add('10:00', 'Мужская стрижка', '666666', '05_03')
#x.read_admin_screan_schedule("14_03")
