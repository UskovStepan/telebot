#from datetime import datetime, timedelta
import app.dateandtimes as date
# from datetime import datetime, timedelta



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
    'button1': f'{date.second_day.strftime("%d_%m")}',
	'button2': f'{date.third_day.strftime("%d_%m")}',
	'button3': f'{date.fourth_day.strftime("%d_%m")}',
	'button4': f'{date.fifth_day.strftime("%d_%m")}'}

time_name = {'item1': '10:00', 'item2': '10:30', 'item3': '11:00', 'item4': '11:30', 'item5': '12:00', 'item6': '12:30', 
'item7': '13:00', 'item8': '13:30', 'item9': '14:00', 'item10': '14:30', 'item11': '15:00', 'item12': '15:30', 'item13': '16:00', 'item14': '16:30', 'item15': '17:00', 'item16': '17:30', 'item17': '18:00', 'item18': '18:30', 'item19': '19:00', 'item20': '19:30', 'item21': '20:00', 'item22': '20:30', 'item23': '21:00', 'item24': '21:30'}

list_procedure_time_30min = ['Челка', 'Ровный срез с мытьем головы']
list_procedure_time_60min = ['Мужская стрижка', 'Ровный срез без мытьем головы', 'Мытье головы+выпрямление']
list_procedure_time_90min = ['Уход "Пломбир"+Стрижка','Мужская+детокс кожи головы', 'Тонирование седены+Мужская стрижка', 'Уход "Рекавери"+Стрижка', 'Уход "Детокс"+Стрижка']
list_procedure_time_120min = ['Рекавери+Детокс+Стрижка', 'Пломбир+Детокс+Стрижка']
			
# def lol(current_time, end_time):
# 	total = 1
# 	result = {}
# 	current_time = start_time
# 	while current_time <= end_time:
# 		result[f"item{total}"] = current_time.strftime("%H:%M")
# 		total += 1
# 		current_time += timedelta(minutes=30)
# 	return result

# start_time = datetime.strptime("10:00", "%H:%M")
# end_time = datetime.strptime("21:30", "%H:%M")
# current_time = start_time

# result_dict = lol(start_time, end_time)
# time_name = result_dict

# print(type(data_name['button2']))
# print(type(time_name['item1']))
# print(type(procedure_name['M3']))