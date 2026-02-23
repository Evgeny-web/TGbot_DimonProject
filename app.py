import asyncio
import os.path
import sys

from config import bot, dispatch, CAR_SHOP_DETAILS

from handlers.routers import *
from aiogram.types import FSInputFile
from pathlib import Path

@router_start_bot.startup()
async def on_startup():
    print(f"Starting bot...")

@router_start_bot.shutdown()
async def shutdown():
    print(f"Shutting down bot...")

dispatch.include_router(router_start_bot)
dispatch.include_router(app_router)

async def main():
    try:
        # skip message users offline
        await bot.delete_webhook(drop_pending_updates=True)
        # start bot
        await dispatch.start_polling(bot)
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        await bot.session.close()

async def test():
    pth = "media/carDetails/Kollector.jpeg"
    print(FSInputFile(pth))

    print(Path(__file__).parent.absolute())

if __name__ == '__main__':
    asyncio.run(main())
    # asyncio.run(test())



