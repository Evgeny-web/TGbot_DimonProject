from aiogram.filters.callback_data import CallbackData


class carDetailsShowCallback(CallbackData, prefix="carDetailsShow"):
    action: str = ""
    carCompany: str = ""
    carModel: str = ""
    callbackLevel: str = ""
    part_id: str = ""

