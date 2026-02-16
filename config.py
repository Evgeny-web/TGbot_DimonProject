import json

from aiogram import Bot, Dispatcher, types, Router

# config parameters
with open('app_configs.json', 'r') as f:
    APP_CONFIGS = json.loads(f.read())

TOKEN_API = APP_CONFIGS["BOT_TOKEN"]

# initialize bot and dispatcher
bot = Bot(TOKEN_API) # out bot agent
dispatch = Dispatcher() # our main router

# text for commands
HELP_COMMAND = """
<b>/start</b> <i>- начать работу с ботом</i>
<b>/help</b> <i>- список команд</i>
<b>/description</b> <i>- описание бота и его возможностей</i>
<b>/ikb</b> <i>- открытие инлайн клавиатуры для удобства</i>

"""

DESCRIPTION = """
Бот по предоставлению информации и продаже деталей собственной разработки 
     <b>Дмитрия Воскресенского</b>.
В данном боте можно будет прочитать о деталях, их предназначении, цене и получить контакты для связи.
"""