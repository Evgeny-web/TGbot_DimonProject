from aiogram.filters import Command
from aiogram import F, types
from aiogram.types import ReplyKeyboardRemove, FSInputFile

# routers and keyboards
from handlers.keyboards import main_kb, getCarBrands_kb
from handlers.routers import app_router

from config import bot, HELP_COMMAND, DESCRIPTION, CONTACTS, START_MSG, CAR_DETAILS_TXT
from utils.paths import Project_Path


# Главные команды при запуске бота

@app_router.message(F.text == "/start")
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=START_MSG, parse_mode="HTML", reply_markup=main_kb)

@app_router.message(Command("help"))
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML")

@app_router.message(Command("description"))
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=DESCRIPTION, parse_mode="HTML")
    await message.delete()

@app_router.message(Command("contacts"))
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=CONTACTS, parse_mode="HTML")
    await message.delete()

@app_router.message(Command("carDetails"))
async def ikb_command(message: types.Message):
    await message.answer(text="Добро пожаловать в Небольшой каталог по продаже деталей!",
                         reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=FSInputFile(Project_Path.get_media(subdir="carDetails", filename="Zapchasti.jpeg")),
                         caption=CAR_DETAILS_TXT,
                         reply_markup=getCarBrands_kb())
    # await bot.send_message(chat_id=message.from_user.id, text=CAR_DETAILS_TXT, parse_mode="HTML", reply_markup=getCarBrands_kb())
    await message.delete()


@app_router.message()
async def char_message(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Я не умею отвечать!\n Выберите действие на клавиатуре!", reply_markup=main_kb)