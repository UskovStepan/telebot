import psycopg
from datetime import datetime, timedelta
import schedule
import time
import app.datatime as day
from app.datatime import second_day, third_day, fourth_day, fifth_day





procedure_name = {'M1': 'Мужская стрижка',
			'M2': 'Мужская+детокс кожи головы',
			'M3': 'Тонирование седены+Мужская стрижка',
			'W1': 'Челка',
			'W2': 'Ровный срез с мытьем головы',
			'W3': 'Ровный срез без мытьем головы',
			'W4': 'Мытье головы+выпрямление',
			'W5': 'Уход "Рекавери"+Стрижка',
			'W6': 'Уход "Детокс"+Стрижка',
			'W7': 'Уход "Пломбир"+Стрижка',
			'W8': 'Рекавери+Детокс+Стрижка',
			'W9': 'Пломбир+Детокс+Стрижка',
			'W10': 'Корни+Тонирование+Стрижка',
			'W11': 'Корни+Длина(Пермамент)+Стрижка'}
    
data_name = {
    'button1': f'{second_day.strftime("%d %b")}',
	'button2': f'{third_day.strftime("%d %b")}',
	'button3': f'{fourth_day.strftime("%d %b")}',
	'button4': f'{fifth_day.strftime("%d %b")}'}


def lol(current_time, end_time):
	total = 1
	result = {}
	current_time = start_time
	while current_time <= end_time:
		result[f"item{total}"] = current_time.strftime("%H:%M")
		total += 1
		current_time += timedelta(minutes=30)
	return result

start_time = datetime.strptime("10:00", "%H:%M")
end_time = datetime.strptime("21:30", "%H:%M")
current_time = start_time

result_dict = lol(start_time, end_time)
time_name = result_dict