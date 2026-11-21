from utils import bot
from handlers import dp, dp_admin
import asyncio


async def main():

    await bot.delete_webhook()
    # await dp.start_polling(bot)
    await dp_admin.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Бот остановлен пользователем.")