import asyncio, os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F

from app.handlers import router

load_dotenv()  # загрузка переменных из .env
TOKEN_API = os.getenv("TOKEN_API")
if not TOKEN_API:
    raise ValueError("TOKEN_API не найден в файле .env")

async def main():
    bot = Bot(TOKEN_API)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')

