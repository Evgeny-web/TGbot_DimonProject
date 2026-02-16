from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.callback_utils import carDetailsShowCallback

getCarModels_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Citroen", callback_data="citroenCarModel"),
         InlineKeyboardButton(text="Ford", callback_data="FordCarModel")],
        [InlineKeyboardButton(text="Back", callback_data="Back")]
    ]
)

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/help")],
        [KeyboardButton(text="/description"), KeyboardButton(text="/ikb")]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Choose action..."
)

# or
# builder = ReplyKeyboardBuilder()
# builder.add(KeyboardButton(text="/give"))
# builder.add(KeyboardButton(text="/description"))
# builder.adjust(2)
#
# kb = builder.as_markup(resize_keyboard=True)


# Ford keyboard choose
def getFordDetailShow_kb(callback_level: str = "carModels_kb"):
    fordDetailShow_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Detail_1", callback_data="fordDetailShow_1"),
             InlineKeyboardButton(text="Detail_2", callback_data="fordDetailShow_2")],
            [InlineKeyboardButton(text="Back", callback_data=callback_level)]
        ]
    )
    
    return fordDetailShow_kb


# Citroen keyboard choose
def getCitroenDetailShow_kb(callback_level: str = "carModels_kb"):
    citroenDetailsShow_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Detail_1", callback_data="citroenDetailsShow_1"),
             InlineKeyboardButton(text="Detail_2", callback_data="citroenDetailsShow_2")],
            [InlineKeyboardButton(text="Back", callback_data=callback_level)]
        ]
    )

    return citroenDetailsShow_kb


# Final keyboard in detail show with buy and bach button
def getFinalDetailChoose_kb(callback_level: str = "carModels_kb"):
    """
    Клавиатура послденего выбора товара. С возможностью задать уровень возврата на определенный уровень.
    Если не задано, то вернется на главный выбор моделей авто
    """
    finalDetailChoose_kb = InlineKeyboardMarkup(
        Inline_keyboard=[
            [InlineKeyboardButton(text="Buy", callback_data="BuyDetail")],
            [InlineKeyboardButton(text="Back", callback_data=callback_level)]
        ]
    )

    return finalDetailChoose_kb

# Inline back button, pass function
def getPassBackButton_kb(callback_level: str = "carModels_kb", ):
    """
    Заглушка для не созданного функционала, предложение вернуться назад
    :param callback_level: Уровень на который нужено вернуться (коллбэк функция)
    :return: экземпляр инлайн клавиатуры
    """
    passBackButton_kb = InlineKeyboardMarkup(
        Inline_keyboard=[
            [InlineKeyboardButton(text="К выбору автомобиля", callback_data="carModels_kb")],
            [InlineKeyboardButton(text="Back", callback_data=callback_level)]
        ]
    )

    return passBackButton_kb