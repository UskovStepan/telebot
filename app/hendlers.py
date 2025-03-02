from aiogram import F, Router
from aiogram.filters import CommandStart,  StateFilter, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import app.keyboards as kb
import app.slovo as sl
import database as db


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
    db.DbMarina.db_user_add(client_name=data['name'], client_surname=data['surname'], client_tg_id=message.from_user.id, client_number_phone=data['number'])
    await state.clear()


"""Кнопка изменить данные, которая проводит регистрацию заново"""
@router.message(F.text =='Изменить данные')
async def registr_step_one(message: Message, state: FSMContext):
    db.DbMarina.delete_incorrect_data(old_id=str(message.from_user.id))
    await state.set_state(Registration.name)
    await message.answer('Введите Ваше имя')


"""Кнопка назад которая возвращает первую клавиатуру"""
@router.message(F.text =='Выйти')
async def get_back(message: Message):
    await message.answer(f'Пожалуйста обязательно ознакомтесь с содержимым под кнопкой "Важно" после заходите в расписание', reply_markup=kb.first_kb)


"""После команды старт, появляются клавиатура из 3 кнопок Price, Important, Schedule"""
@router.message(F.text =='Цены')
async def get_help(message: Message):
    await message.answer_photo(photo = 'https://github.com/UskovStepan/telebot/blob/master/Price.jpg?raw=true', caption = "Пожалуйста внимательно ознакомьтесь с ценами!")

@router.message(F.text =='Важно')
async def must_read(message: Message):
    await message.answer_photo(photo = 'https://github.com/UskovStepan/telebot/blob/master/Help.jpg?raw=true')

#________________________________________________________________
#Клавиатуры расписания и выбора процедуры
     
"""После нажитаия на кнопку расписания появляется inLine клавиатура выбора Мужские&Женские"""
"""Обработчик записи клиента на стрижку"""  
class Registration_data(StatesGroup):
    client_id = State()
    date = State()
    time = State()
    procedure = State()


@router.message(F.text == 'Расписание')
async def schedule(message: Message, state: FSMContext):
    id = message.from_user.id
    if db.DbMarina.search_for_an_existing(id) is not None:
        await message.answer(f'Вы записаны на: {db.DbMarina.search_for_an_existing(id)[0]}\nВремя записи: {db.DbMarina.search_for_an_existing(id)[1]}\nНа процедуру: {db.DbMarina.search_for_an_existing(id)[2]}')
    await message.answer(f'{message.from_user.first_name} выбурите на какую процедуру вы бы хотели записаться!', reply_markup=kb.selecting_a_procedure)
    await state.set_state(Registration_data.procedure)


@router.callback_query(Registration_data.procedure)
async def procedure_selection(callback: CallbackQuery, state: FSMContext):
    await state.update_data(procedure = str(callback.data))
    await callback.message.edit_text(f'Выберите день записи:', reply_markup=kb.data_choice)
    await state.set_state(Registration_data.date)


"""Записаться можно на 4 будующих дня, поэтому в меню Schedule 4 кнопки выбора дня и одна кнопка назад возвращающая пользователя к выбору дня"""
@router.callback_query(Registration_data.date)
async def procedure_selection(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date = str(callback.data))
    free_time_chooise= db.DbMarina.screan_schedule(sl.data_name[callback.data])
    free_time_chooise_keyboards = kb.create_time_keyboard(free_time_chooise)
    await callback.message.edit_text(f'Время для записи', reply_markup=free_time_chooise_keyboards)
    await state.set_state(Registration_data.time)


"""Регистрация данных о записи в базу данных и очистка state"""
@router.callback_query(Registration_data.time)
async def procedure_selection_steptow(callback: CallbackQuery, state: FSMContext):
    await state.update_data(time = str(callback.data))
    data = await state.get_data()
    await callback.message.edit_text(f'''Спасибо! Вы записанны на:\nДата: {sl.data_name[str(data["date"])]}\nВремя: {sl.time_name[str(data['time'])]}\nНа процедуру: {sl.procedure_name[str(data['procedure'])]}\nВам прийдет напоминание в день посещения и за час до начала.''')
    db.DbMarina.db_schedule_add(client_id = callback.message.from_user.id, date = sl.data_name[data['date']], recorder_time = sl.time_name[data['time']], procedure = sl.procedure_name[data['procedure']])
    print(f'''Дата: {sl.data_name[str(data["date"])]}\nВремя: {sl.time_name[str(data['time'])]}\nПроцедура: {sl.procedure_name[str(data['procedure'])]}''')
    await state.clear()
   

@router.callback_query(F.data == 'button5')
async def catalog_day_four(callback:CallbackQuery): 
    await callback.message.edit_text(f'{callback.message.from_user.first_name} Выбурите какие виды процедур Вам нужны!', reply_markup=kb.selecting_a_procedure)

@router.callback_query(F.data == 'step_back')
async def step_back(callback: CallbackQuery):
    await callback.answer(f'Назад')
    await callback.message.edit_text(f'{callback.from_user.first_name} выбери дату!', reply_markup=kb.data_choice)
