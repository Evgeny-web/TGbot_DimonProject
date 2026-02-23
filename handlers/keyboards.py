from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from utils.callback_utils import carDetailsShowCallback
from config import CAR_SHOP_DETAILS

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/help")],
        [KeyboardButton(text="/description"), KeyboardButton(text="/contacts")],
        [KeyboardButton(text="/carDetails")]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Choose action..."
)


def getCarBrands_kb():
    """
    Клавиатура с брендами машин для магазина деталей (уровень 1)
    :return: InlineKeyboardBuilder
    """
    carBrands_kb = InlineKeyboardBuilder()

    for car in list(CAR_SHOP_DETAILS.keys()):
        carBrands_kb.button(
            text=car,
            callback_data=carDetailsShowCallback(
                action="show",
                carBrand=car,
                callbackLevel="get_car_brands",
                callbackLevelNext="get_car_details"
            ).pack()
        )

    carBrands_kb.button(text="Main menu", callback_data="main_menu")

    # edit 2 columns in row
    carBrands_kb.adjust(2)

    return carBrands_kb.as_markup()


def getCarDetails_kb(callback_data: carDetailsShowCallback):
    """
    Клавиатура для получения деталей конкретной марки авто (уровень 2)
    :param car_brand: Марка авто
    :return: InlineKeyboardBuilder
    """
    carDetails_kb = InlineKeyboardBuilder()
    car_brand = callback_data.carBrand
    brand_details = CAR_SHOP_DETAILS.get(car_brand, {}).get("details", {})

    for detail in list(brand_details.keys()):
        carDetails_kb.button(
            text=detail,
            callback_data=carDetailsShowCallback(
                action="show",
                carBrand=car_brand,
                carDetail=detail,
                callbackLevel=callback_data.callbackLevelNext,
                callbackLevelNext="get_detail"
            ).pack()
        )

    carDetails_kb.button(
        text="Back",
        callback_data=carDetailsShowCallback(
            action="show",
            carBrand=car_brand,
            callbackLevel=callback_data.callbackLevelNext,
            callbackLevelNext=callback_data.callbackLevel
        ).pack()
    )

    # edit 2 column in row
    carDetails_kb.adjust(2)

    return carDetails_kb.as_markup()


# Final keyboard in detail show with buy and bach button
def getDetail_kb(callback_data: carDetailsShowCallback):
    """
    Клавиатура на уровне товара (уровень 3).
    Выбор купить, назад или к выбору марки авто
    """
    finalDetailChoose_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Buy", callback_data=carDetailsShowCallback(
                    action="buy",
                    carBrand=callback_data.carBrand,
                    carDetail=callback_data.carDetail,
                    callbackLevel=callback_data.callbackLevelNext,
                    callbackLevelNext="buy_detail"
                ).pack())
            ],
            [
                InlineKeyboardButton(text="Back", callback_data=carDetailsShowCallback(
                    action="show",
                    carBrand=callback_data.carBrand,
                    callbackLevel=callback_data.callbackLevelNext,
                    callbackLevelNext=callback_data.callbackLevel
                    ).pack()
                ),
                 InlineKeyboardButton(text="Car brands", callback_data=carDetailsShowCallback(
                     action="show",
                     callbackLevel=callback_data.callbackLevelNext,
                     callbackLevelNext="get_car_brands"
                    ).pack()
                )
            ],
            [
                InlineKeyboardButton(text="Main menu", callback_data="main_menu")
            ]
        ],

    )

    return finalDetailChoose_kb


def getBuyDetail_kb(callback_data: carDetailsShowCallback):
    """
    Клавиатура на уровне покупки детали для авто.
    Выбор: Главное меню, выборк марки авто
    :return: InlineKeyboardMarkup
    """

    buy_detail_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Car brands", callback_data=carDetailsShowCallback(
                     action="show",
                     callbackLevel=callback_data.callbackLevelNext,
                     callbackLevelNext="get_car_brands"
                    ).pack()),
                InlineKeyboardButton(text="Main menu", callback_data="main_menu")
            ]
        ]
    )

    return buy_detail_kb