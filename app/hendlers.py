from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
import app.datatime as dt

router = Router()
marina = '@Smarnie'


@router.message(CommandStart())
async def cmd_start(message: Message):
	await message.answer(f'Привет {message.from_user.first_name} {message.from_user.last_name}! Я помогу тебе записаться к {marina}, расскажу тебе о ценах на услуги и напомню о записи за час!', reply_markup=kb.first_kb)


@router.message(Command('price'))
async def get_help(message: Message):
    await message.answer_photo(photo = 'https://github.com/UskovStepan/telebot/blob/master/Price.jpg?raw=true', caption = "Пожалуйста внимательно ознакомьтесь с ценами!")

@router.message(Command('important'))
async def must_read(message: Message):
    await message.answer_photo(photo = 'https://github.com/UskovStepan/telebot/blob/master/Help.jpg?raw=true')

@router.message(Command('schedule'))
async def schedule(message: Message):
	await message.answer(f'{message.from_user.first_name} выбери дату!', reply_markup=kb.data_choice)

@router.callback_query(F.data == 'button1')
async def catalog(callback:CallbackQuery):
    await callback.answer(f'Вы выбрали {dt.now.strftime("%d %b")}')  
    await callback.message.edit_text('Выберите пожалуйста подходящее время, в случае если время вам не подходит попробудет выбрать другой день', reply_markup=kb.time_choice)