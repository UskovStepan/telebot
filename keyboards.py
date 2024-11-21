from aiogram.types import (
	ReplyKeyboardMarkup,
	KeyboardButton,
	InlineKeyboardMarkup,
	InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from datatime import second_day, third_day, fourth_day
#first_day, fifth_day, sixth_day, seventh_day 

first_kb = ReplyKeyboardMarkup(
	keyboard=[[KeyboardButton(text='Обязательно к прочтению')],
				[KeyboardButton(text='Расписание'),KeyboardButton(text='Цена')]], 
resize_keyboard=True, input_field_placeholder='Информационное окно', selective=True)

data_choice = InlineKeyboardMarkup(
	inline_keyboard=[
		[InlineKeyboardButton(text=f'{second_day.strftime('%d %b')}')], [InlineKeyboardButton(text=f'{third_day.strftime('%d %b')}')], 		
		[InlineKeyboardButton(text=f'{fourth_day.strftime('%d %b')}')], [InlineKeyboardButton(text=f'{fourth_day.strftime('%d %b')}') ]]
	)

class Pagination(CallbackData, prefix ='pag'):
	action: str
	page: int

def paginator(page: int = 0):
	builder = InlineKeyboardBuilder()
	builder.row(
		InlineKeyboardButton(text='Назад', callback_data=Pagination(action="prev", page=page).pack()),
		InlineKeyboardButton(text='Вперед', callback_data=Pagination(action="next", page=page).pack())
	)
	return builder.as_markup()