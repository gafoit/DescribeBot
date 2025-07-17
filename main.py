import asyncio
import logging
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from Bot.bot import bot, dp
from Bot import config
from Bot.handlers import start, info

# Логирование
logging.basicConfig(level=logging.INFO)

# Роутеры
dp.include_router(start.router)
dp.include_router(info.router)


async def on_startup():
    await bot.set_webhook(config.WEBHOOK_URL, secret_token=config.WEBHOOK_SECRET)


async def on_shutdown():
    await bot.delete_webhook()


async def create_app():
    app = web.Application()
    app["bot"] = bot

    # Для обработки входящих запросов
    webhook_requests_handler = SimpleRequestHandler(dispatcher=dp, bot=bot, secret_token=config.WEBHOOK_SECRET)
    webhook_requests_handler.register(app, path=config.WEBHOOK_PATH)

    setup_application(app, dp, on_startup=on_startup, on_shutdown=on_shutdown)
    return app


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = loop.run_until_complete(create_app())
    web.run_app(app, port=8000)
