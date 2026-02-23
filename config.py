import json

from aiogram import Bot, Dispatcher, types, Router

# config parameters
with open('app_configs.json', 'r') as f:
    APP_CONFIGS = json.loads(f.read())

# Parameters cars shop
with open('CarDetails.json', 'r') as f:
    CAR_SHOP_DETAILS = json.loads(f.read())

TOKEN_API = APP_CONFIGS["BOT_TOKEN"]

# initialize bot and dispatcher
bot = Bot(TOKEN_API) # out bot agent
dispatch = Dispatcher() # our main router

# text for commands
START_MSG = """
Добро пожаловать в <b>ДиВо_Деталь_БОТ</b>!

Здесь можно узнать о деталях собственной разработки и продажи
    <b>Дмитрия Воскресенского</b>.
    
Более подробная информация по кнопке /description.
"""

HELP_COMMAND = """
<b>/start</b> -<i> начать работу с ботом</i>
<b>/help</b> -<i> список команд</i>
<b>/description</b> -<i> описание бота и его возможностей</i>
<b>/contacts</b> - <i>контактная информация</i>
<b>/carDetails</b> - <i>магазин деталей</i>
"""

DESCRIPTION = """
Бот по предоставлению информации и продаже деталей собственной разработки 
     <b>Дмитрия Воскресенского</b>.
В данном боте можно будет прочитать о деталях, их предназначении, цене и получить контакты для связи.
"""

CONTACTS = """
Здесь вся необходимая контактная информация.

Куда звонить и писать, почта или что-то еще.
Телефон: 8-___
Почта: ___@email.com
Адрес, где забирать детали: ул. Кошки, д. Собачки
"""

CAR_DETAILS_TXT = """
В данный момент доступны детали для следующих марок авто: (выберите подходящую)
"""