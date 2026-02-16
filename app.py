import asyncio
import sys

from config import bot, dispatch

from handlers.routers import *

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

if __name__ == '__main__':
    asyncio.run(main())



