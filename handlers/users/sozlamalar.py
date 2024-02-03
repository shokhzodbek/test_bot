from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.menu import lang
from loader import dp 

@dp.message_handler(Command("sozlamalar"))
async def bot_sozlamalar(message:types.Message):
    await message.answer(f"sozlamalar, {message.from_user.full_name}!",reply_markup=lang)



@dp.message_handler(Command("darslar"))
async def bot_daralar(message:types.Message):
    await message.answer(f"darstlar, {message.from_user.full_name}!")




@dp.message_handler(Command("knobka"))
async def bot_knobka(message:types.Message):
    await message.answer(f"Knobka, {message.from_user.full_name}!")
