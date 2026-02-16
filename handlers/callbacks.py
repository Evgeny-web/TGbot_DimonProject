from aiogram import F, types

from handlers.routers import app_router
from handlers.keyboards import getCitroenDetailShow_kb, getFinalDetailChoose_kb, getFordDetailShow_kb, getCarModels_kb, getPassBackButton_kb
from config import bot
from utils.callback_utils import carDetailsShowCallback


# callback for main menu choose car for details
@app_router.callback_query(F.data == "carModels_kb")
async def carModels_kb(callback: types.CallbackQuery):
    await callback.message.edit_text(f"Здесь будет представлен модельный ряд автомобилей, к которым имеются детали для продажи.\n"
                                     f"Можно указывать не просто марки, а год, кузов и др. (или зделать еще одну вложенность для этого).",
                                     reply_markup=getCarModels_kb)
    await callback.answer()


# Details for Ford cars

@app_router.callback_query(F.data == "fordCarModel")
async def fordCarModel(callback: types.CallbackQuery):
    await callback.message.edit_text(f"Детали для автомобилей форд",
                                     reply_markup=getFordDetailShow_kb())
    await callback.answer()


@app_router.callback_query(F.data == "fordDetailShow_1")
async def fordDetailShow_1(callback: types.CallbackQuery):
    photo_url = "https://www.megway.ru/sites/default/files/11112.jpeg"
    caption = ("**Turbina!**\n\n"
               "Придумал собственный сплав, выдержит любые нагрузки и температуры!\n\n"
               "**Цена:** 3B")
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo_url,
            caption=caption,
            parse_mode="Markdown"
        ),
        reply_markup=getFinalDetailChoose_kb(callback_level="fordCarModel")
    )
    await callback.answer()

@app_router.callback_query(F.data == "fordDetailShow_2")
async def fordDetailShow_2(callback: types.CallbackQuery):
    photo_url = "https://www.amry.ru/_upload/detail_pics/SH%20AUTO%20PARTS/SH39100.jpg"
    caption = ("**Richag!**\n\n"
               "Согнул из того что было, сначал спину чесал, но потом ниче так деталь оказалась!\n\n"
               "**Цена: **4B")

    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo_url,
            caption=caption,
            parse_mode="Markdown"
        ),
        reply_markup=getFinalDetailChoose_kb(callback_level="fordCarModel")
    )
    await callback.answer()


#  Details for Citroen cars

@app_router.callback_query(F.data == "citroenCarModel")
async def citroenCarModel(callback: types.CallbackQuery):
    await callback.message.edit_text(f"Здесь будет представлен выбор деталей для клиента.\n "
                                     f"У меня их нет, пока будут просто детали)",
                                     reply_markup=getCitroenDetailShow_kb())
    await callback.answer()

@app_router.callback_query(F.data == "citroenDetailsShow_1")
async def citroenDetailsShow_1(callback: types.CallbackQuery):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf4OLrTgiwzZR--1dYucALMHNZ6HBUX7LXaw&s"
    caption = ("**Pompa**\n\n "
               "Я ее придумал, когда мне было 12 лет.\n "
               "Испытал уже на более 1000 автомобилей..."
               "**Price** : 1B")

    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo_url,
            caption=caption,
            parse_mode="Markdown"
        ),
        reply_markup=getFinalDetailChoose_kb(callback_level="citroenCarModel")
    )
    await callback.answer()

@app_router.callback_query(F.data == "citroenDetailsShow_2")
async def citroenDetailsShow_1(callback: types.CallbackQuery):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtMM4DD_touLnNtUOYXPkbfbw6f-BJyAWy6g&s"
    caption = ("**Kollector** \n\n "
               "Приснилось, когда мне было 16 лет.\n "
               "Испытал уже на более 500 автомобилей..."
               "**Price** : 2B")

    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo_url,
            caption=caption,
            parse_mode="Markdown"
        ),
        reply_markup=getFinalDetailChoose_kb(callback_level="citroenCarModel")
    )
    await callback.answer()


@app_router.callback_query(F.data == "BuyDetail")
async def BuyDetail(callback: types.CallbackQuery):
    await callback.message.edit_text(text=f"Здесь пока пусто! В будущем здесь можно развить функционал покупки.\n"
                                          f"сервис или просто контакты",
                                     reply_markup=getPassBackButton_kb())
    await callback.answer()

