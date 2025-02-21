from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.datatime as dt

router = Router()

marina = '@Smarnie'


"""Обработчик команды старт"""
@router.message(CommandStart())
async def cmd_start(message: Message):
	await message.answer(f'Привет {message.from_user.first_name} {message.from_user.last_name}! Я помогу тебе записаться к {marina}, расскажу тебе о ценах на услуги и напомню о записи за час! Пожалуйста не забудьте пройти регистрацию!', reply_markup=kb.first_kb)
     
"""Обработка регистрации ползователя"""
class Registration(StatesGroup):
    name = State()
    surname = State()
    number = State()     
     
@router.message(F.text == 'Регистрация')
async def registr_step_one(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer('Введите Ваше имя')

@router.message(Registration.name)
async def registr_step_tow(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.surname)
    await message.answer('Введите Вашу Фамилию')

@router.message(Registration.surname)
async def registr_step_three(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await state.set_state(Registration.number)
    await message.answer('Просто нажмите на кнопку "Отправить номер"', reply_markup=kb.get_number)

@router.message(Registration.number, F.contact)
async def registr_step_tow(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Спасибо за регистрацию! \nИмя: {data['name']}\nФамилия: {data['surname']}\nНомер: {data['number']}\nПожалуйста проверьте верно ли введены данные, в случае ошибки пройдите регистрацию заново')
    await state.clear()

"""Кнопка назад которая возвращает первую клавиатуру"""
@router.message(F.text =='Назад')
async def get_help(message: Message):
    await message.answer(f'Пожалуйста обязательно ознакомтесь с содержимым под кнопкой "Важно" после заходите в расписание', reply_markup=kb.first_kb)


"""После команды старт, появляются клавиатура из 3 кнопок Price, Important, Schedule"""
@router.message(F.text =='Цены')
async def get_help(message: Message):
    await message.answer_photo(photo = 'https://github.com/UskovStepan/telebot/blob/master/Price.jpg?raw=true', caption = "Пожалуйста внимательно ознакомьтесь с ценами!")

@router.message(F.text =='Важно')
async def must_read(message: Message):
    await message.answer_photo(photo = 'https://github.com/UskovStepan/telebot/blob/master/Help.jpg?raw=true')

@router.message(F.text == 'Расписание')
async def schedule(message: Message):
	await message.answer(f'{message.from_user.first_name} выбери дату!', reply_markup=kb.data_choice)
     
"""Записаться можно на 4 будующих дня, поэтому в меню Schedule 4 кнопки выбора дня и одна кнопка назад возвращающая пользователя к выбору дня"""
@router.callback_query(F.data == 'button1')
async def catalog_day_one(callback:CallbackQuery):
    await callback.answer(f'Вы выбрали {dt.second_day.strftime("%d %b")}')  
    await callback.message.edit_text('Выберите пожалуйста подходящее время, в случае если время вам не подходит или его нет совсем, попробудет выбрать другой день', reply_markup=kb.time_choice)

@router.callback_query(F.data == 'button2')
async def catalog_day_tow(callback:CallbackQuery):
    await callback.answer(f'Вы выбрали {dt.third_day.strftime("%d %b")}')  
    await callback.message.edit_text('Выберите пожалуйста подходящее время, в случае если время вам не подходит или его нет совсем, попробудет выбрать другой день', reply_markup=kb.time_choice)
    
@router.callback_query(F.data == 'button3')
async def catalog_day_three(callback:CallbackQuery):
    await callback.answer(f'Вы выбрали {dt.fourth_day.strftime("%d %b")}')  
    await callback.message.edit_text('Выберите пожалуйста подходящее время, в случае если время вам не подходит или его нет совсем, попробудет выбрать другой день', reply_markup=kb.time_choice)

@router.callback_query(F.data == 'button4')
async def catalog_day_four(callback:CallbackQuery):
    await callback.answer(f'Вы выбрали {dt.fifth_day.strftime("%d %b")}')  
    await callback.message.edit_text('Выберите пожалуйста подходящее время, в случае если время вам не подходит или его нет совсем, попробудет выбрать другой день', reply_markup=kb.time_choice)

@router.callback_query(F.data == 'step_back')
async def step_back(callback: CallbackQuery):
    await callback.answer(f'Назад')
    await callback.message.edit_text(f'{callback.from_user.first_name} выбери дату!', reply_markup=kb.data_choice)
