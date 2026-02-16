from aiogram.filters import Command
from aiogram import F, types

# routers and keyboards
from handlers.keyboards import kb, ikb
from handlers.routers import app_router

from config import bot, HELP_COMMAND, DESCRIPTION

@app_router.message(F.text == "/start")
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Добро пожаловать в ДиВо_Деталь_БОТ!", reply_markup=kb)
    await message.delete()

@app_router.message(Command("help"))
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()

@app_router.message(Command("description"))
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=DESCRIPTION, parse_mode="HTML")
    await message.delete()

@app_router.message(Command("ikb"))
async def ikb_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Inline keyboard", reply_markup=ikb)
    await message.delete()


@app_router.message()
async def char_message(message: types.Message):
    count_gal = message.text.count("✅")
    await message.answer(text=f"✅ in your message is {count_gal}")