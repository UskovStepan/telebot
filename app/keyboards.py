from aiogram.types import (
	ReplyKeyboardMarkup,
	KeyboardButton,
	InlineKeyboardMarkup,
	InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime, timedelta

from aiogram.filters.callback_data import CallbackData
import app.dateandtimes as date



first_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Важно'), KeyboardButton(text='Цены')],
										[KeyboardButton(text='Запись'),KeyboardButton(text='Регистрация')]], 
resize_keyboard=True, input_field_placeholder='Выберите пункт в меню') #, selective=True)


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Отправить номер', request_contact=True), KeyboardButton(text='Изменить данные')], [KeyboardButton(text='Выйти')] ], resize_keyboard=True)


data_choice = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text=f'{date.second_day.strftime("%d %b")}', callback_data='button1'), 
		InlineKeyboardButton(text=f'{date.third_day.strftime("%d %b")}', callback_data='button2')
	], 		
	[
		InlineKeyboardButton(text=f'{date.fourth_day.strftime("%d %b")}', callback_data='button3'), 
		InlineKeyboardButton(text=f'{date.fifth_day.strftime("%d %b")}', callback_data='button4')
	],
	[
		InlineKeyboardButton(text='Назад', callback_data='button5')
	]
	])

def create_time_keyboard(result):
	builder = InlineKeyboardBuilder()
	item = 0
	for time, is_broked in result.items():
		item += 1
		if not is_broked:
			builder.add(InlineKeyboardButton(text=time, callback_data= f'item{item}'))
	builder.adjust(3)
	return builder.as_markup()

	
time_choice = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text='10:00', callback_data= 'item1'), 
		InlineKeyboardButton(text='10:30', callback_data='item2'), 
		InlineKeyboardButton(text='11:00', callback_data='item3')
	],
	[
		InlineKeyboardButton(text='11:30', callback_data= 'item4'), 
		InlineKeyboardButton(text='12:00', callback_data='item5'), 
		InlineKeyboardButton(text='12:30', callback_data='item6')
	],
	[
		InlineKeyboardButton(text='13:00', callback_data= 'item7'), 
		InlineKeyboardButton(text='13:30', callback_data='item8'), 
		InlineKeyboardButton(text='14:00', callback_data='item9')
	],
	[
		InlineKeyboardButton(text='14:30', callback_data= 'item10'), 
		InlineKeyboardButton(text='15:00', callback_data='item11'), 
		InlineKeyboardButton(text='15:30', callback_data='item12')
	],
	[
		InlineKeyboardButton(text='16:00', callback_data= 'item13'), 
		InlineKeyboardButton(text='16:30', callback_data='item14'), 
		InlineKeyboardButton(text='17:00', callback_data='item15')
	],
	[
		InlineKeyboardButton(text='17:30', callback_data= 'item16'), 
		InlineKeyboardButton(text='18:00', callback_data='item17'), 
		InlineKeyboardButton(text='18:30', callback_data='item18')
	],
	[
		InlineKeyboardButton(text='19:00', callback_data= 'item19'), 
		InlineKeyboardButton(text='19:30', callback_data='item20'), 
		InlineKeyboardButton(text='20:00', callback_data='item21')
	],
	[
		InlineKeyboardButton(text='20:30', callback_data= 'item22'), 
		InlineKeyboardButton(text='21:00', callback_data='item23'), 
		InlineKeyboardButton(text='21:30', callback_data='item24')
	],
	[
		InlineKeyboardButton(text='Назад', callback_data= 'step_back')
	]])


selecting_a_procedure = InlineKeyboardMarkup(inline_keyboard=[
	[InlineKeyboardButton(text='Мужская стрижка', callback_data='M1')],
	[InlineKeyboardButton(text='Мужская+детокс кожи головы', callback_data='M2')],
	[InlineKeyboardButton(text='Тонирование седены+Мужская стрижка', callback_data='M3')],
	[InlineKeyboardButton(text='Челка', callback_data='W1')],
	[InlineKeyboardButton(text='Ровный срез с мытьем головы', callback_data='W2')],
	[InlineKeyboardButton(text='Ровный срез без мытьем головы', callback_data='W3')],
	[InlineKeyboardButton(text='Мытье головы+выпрямление', callback_data='W4')],
	[InlineKeyboardButton(text='Уход "Рекавери"+Стрижка', callback_data='W5')],
	[InlineKeyboardButton(text='Уход "Детокс"+Стрижка', callback_data='W6')],
	[InlineKeyboardButton(text='Уход "Пломбир"+Стрижка', callback_data='W7')],
	[InlineKeyboardButton(text='Рекавери+Детокс+Стрижка', callback_data='W8')],
	[InlineKeyboardButton(text='Пломбир+Детокс+Стрижка', callback_data='W9')]
])

admin_first = ReplyKeyboardMarkup(keyboard=[
	[KeyboardButton(text='Расписание'), KeyboardButton(text='Черный список')]
], resize_keyboard=True)


admin_schedule = ReplyKeyboardMarkup(keyboard=[
	[KeyboardButton(text='Посмотреть расписание'), KeyboardButton(text='Удалить запись')],
	[KeyboardButton(text='Остановить запись'), KeyboardButton(text='Возобновить запись')],
	[KeyboardButton(text='Изменить запись'), KeyboardButton(text = 'Назад')]
], resize_keyboard=True)

admin_blacklist = ReplyKeyboardMarkup(keyboard=[
	[KeyboardButton(text='Добавить'), KeyboardButton(text='Удалить')]
], resize_keyboard=True)

class MyCallbackFactory(CallbackData, prefix = 'my_factory'):
	number: int

admin_data_choice = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text=f'{date.now.strftime("%d %b")}', callback_data='abutton1'),
		InlineKeyboardButton(text=f'{date.second_day.strftime("%d %b")}', callback_data='abutton2')
	], 
	[
		InlineKeyboardButton(text=f'{date.third_day.strftime("%d %b")}', callback_data='abutton3'), 	InlineKeyboardButton(text=f'{date.fourth_day.strftime("%d %b")}', callback_data='abutton4')
	], 
	[
		InlineKeyboardButton(text=f'{date.fifth_day.strftime("%d %b")}', callback_data='abutton4'),InlineKeyboardButton(text='Назад', callback_data='a_button6')
	]
	])


def build_actions_kb():
	builder = InlineKeyboardBuilder()
	time = date.now
	for i in range(5):
		time_in = time.strftime("%d %b")
		builder.add(InlineKeyboardButton(text=time_in, callback_data= f'a_item{i}'))
		time += timedelta(days=1)
	builder.add(InlineKeyboardButton(text='Назад', callback_data='a_back'))
	builder.adjust(2)
	return builder.as_markup()