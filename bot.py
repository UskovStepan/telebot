import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

import keyboards

kb = keyboards

bot = Bot('7901916608:AAEUmjTFjM9a0amlNnEtlY438FAn6y-lqko')
dp = Dispatcher()
marina = '@Smarnie'

@dp.message(CommandStart())
async def start(message: Message):
	await message.answer(f'Привет {message.from_user.first_name} {message.from_user.last_name}! Я помогу тебе записаться к {marina}, расскажу тебе о ценах на услуги и напомню о записи за час!', reply_markup=kb.first_kb)

@dp.message()
async def echo(message:Message):
	file_ids = []
	msg = message.text.lower()
	if msg == 'Обязательно к прочтению':
		file_path = 'Help.jpg'



async def main():
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)
	

if __name__ == '__main__':
	asyncio.run(main())