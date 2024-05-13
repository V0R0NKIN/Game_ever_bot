import asyncio
import logging
import sys
from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher, exceptions, types
from app.tool import viselnitsa, tool_viselnitsa
from settings import bot_token
from app.handlers import router




bot = Bot(token=bot_token)

dp = Dispatcher()
dp.include_router(router)
dp.include_router(viselnitsa.router)

async def main() -> None:

    await bot.set_my_commands(commands=[
        BotCommand(command="start", description='Старт bot'),
        BotCommand(command="infa", description='Інформація')
    ])
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
