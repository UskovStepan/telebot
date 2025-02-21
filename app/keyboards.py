from aiogram.types import (
	ReplyKeyboardMarkup,
	KeyboardButton,
	InlineKeyboardMarkup,
	InlineKeyboardButton)

#from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
#from aiogram.filters.callback_data import CallbackData
from app.datatime import second_day, third_day, fourth_day, fifth_day
#first_day, sixth_day, seventh_day 


first_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Важно'), KeyboardButton(text='Регистрация')],
										[KeyboardButton(text='Расписание'),KeyboardButton(text='Цены')]], 
resize_keyboard=True, input_field_placeholder='Выберите пункт в меню') #, selective=True)


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Отправить номер', request_contact=True), KeyboardButton(text='Назад')]], resize_keyboard=True)


data_choice = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text=f'{second_day.strftime("%d %b")}', callback_data='button1'), 
		InlineKeyboardButton(text=f'{third_day.strftime("%d %b")}', callback_data='button2')
	], 		
	[
		InlineKeyboardButton(text=f'{fourth_day.strftime("%d %b")}', callback_data='button3'), 
		InlineKeyboardButton(text=f'{fifth_day.strftime("%d %b")}', callback_data='button4')
	]
	])
	
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




#Пагинация, используется для перебора каких нибудь сисков и тп. Удобно для меню товаров
# class Pagination(CallbackData, prefix ='pag'):
# 	action: str
# 	page: int

# def paginator(page: int = 0):
# 	builder = InlineKeyboardBuilder()
# 	builder.row(
# 		InlineKeyboardButton(text='Назад', callback_data=Pagination(action="prev", page=page).pack()),
# 		InlineKeyboardButton(text='Вперед', callback_data=Pagination(action="next", page=page).pack()),
# 		width=2
# 	)
# 	return builder.as_markup()