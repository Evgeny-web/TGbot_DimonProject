from aiogram import F, types
from aiogram.types import FSInputFile

from handlers.routers import app_router
from handlers.keyboards import getCarBrands_kb, getCarDetails_kb, getDetail_kb, getBuyDetail_kb, main_kb

from config import bot, CAR_DETAILS_TXT, CAR_SHOP_DETAILS
from utils.callback_utils import carDetailsShowCallback
from utils.paths import Project_Path


@app_router.callback_query(F.data == "main_menu")
async def main_menu(callback: types.CallbackQuery):
    await callback.message.answer(text="Main menu!",
                                  reply_markup=main_kb)
    await callback.message.delete()
    await callback.answer()


@app_router.callback_query(carDetailsShowCallback.filter(F.callbackLevelNext == "get_car_brands"))
async def show_car_brands(callback: types.CallbackQuery, callback_data: carDetailsShowCallback):
    """
    Показывает клавиатуру с брендами автомобилей
    callbackLevel = get_car_brands
    коллбэк для начального состояния, для возврата, потому что изначально это задается через хэндлер клавиатуры
    """
    caption = (CAR_DETAILS_TXT)
    photo = Project_Path.get_media(subdir=f"carDetails", filename=f"Zapchasti.jpeg")

    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=FSInputFile(photo),
            caption=caption,
            parse_mode="Markdown"
        ),
        reply_markup=getCarBrands_kb()
    )
    await callback.answer()


@app_router.callback_query(carDetailsShowCallback.filter(F.callbackLevelNext == "get_car_details"))
async def show_car_details(callback: types.CallbackQuery, callback_data: carDetailsShowCallback):
    """
    Показывает детали для выбранной марки авто
    callbackLevel = get_car_details
    это коллбек, который должен возвращаться уже в ответ на марку авто
    показывает детали, дает выбор (детали, назад, главное меню)
    """
    car_brand = callback_data.carBrand
    caption = (f"Выберите деталь для бренда авто **{car_brand}**")
    photo_brand = Project_Path.get_media(subdir=f"carBrand", filename=f"{car_brand}.jpg")

    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=FSInputFile(photo_brand),
            caption=caption,
            parse_mode="Markdown"
        ),
        reply_markup=getCarDetails_kb(callback_data)
    )
    await callback.answer()


@app_router.callback_query(carDetailsShowCallback.filter(F.callbackLevelNext == "get_detail"))
async def show_car_detail_info(callback: types.CallbackQuery, callback_data: carDetailsShowCallback):
    """
    Показывает информацию о выбранной детали
    callbackLevel = get_car_details
    это коллбэк, который уже показывает информацию о детали, и дает выбор купить или вернуться (назад, выбор марки, главное меню)
    """
    car_brand = callback_data.carBrand
    car_detail = callback_data.carDetail

    # get JSON value
    detail_info = CAR_SHOP_DETAILS.get(car_brand, {}).get("details", {}).get(car_detail, {})

    # Формируем сообщение
    detail_photo = Project_Path.get_media(subdir="carDetails", filename=detail_info.get("photo_detail", ""))
    caption = (
        f"**{detail_info['name_detail']}**\n\n"
        f"{detail_info['desc_detail']}\n\n"
        f"**Цена:** {detail_info['Price_detail']}"
    )

    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=FSInputFile(detail_photo),
            caption=caption,
            parse_mode="Markdown"
        ),
        reply_markup=getDetail_kb(callback_data)
    )
    await callback.answer()


# Buy detail
@app_router.callback_query(carDetailsShowCallback.filter(F.callbackLevelNext == "buy_detail"))
async def buy_car_detail(callback: types.CallbackQuery, callback_data: carDetailsShowCallback):
    """
    коллбэк для покупки детали
    """
    await callback.message.edit_caption(caption=f"Здесь пока пусто! В будущем здесь можно развить функционал покупки.\n"
                                          f"сервис или просто контакты",
                                     reply_markup=getBuyDetail_kb(callback_data))
    await callback.answer()

