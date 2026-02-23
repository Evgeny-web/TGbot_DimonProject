from aiogram.filters.callback_data import CallbackData


class carDetailsShowCallback(CallbackData, prefix="carDetailsShow"):
    action: str = ""
    carBrand: str = ""
    carDetail: str = ""
    callbackLevel: str = ""
    callbackLevelNext: str = ""

