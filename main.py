import asyncio
import logging
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from Bot.bot import bot, dp
from Bot import config
from Bot.handlers import start, info

logging.basicConfig(level=logging.INFO)

dp.include_router(start.router)
dp.include_router(info.router)


async def on_startup():
    logging.info(f"Setting webhook to {config.WEBHOOK_URL}")
    await bot.set_webhook(config.WEBHOOK_URL, secret_token=config.WEBHOOK_SECRET)


async def on_shutdown():
    logging.info("Deleting webhook")
    await bot.delete_webhook()


async def create_app():
    app = web.Application()
    app["bot"] = bot

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=config.WEBHOOK_SECRET
    )
    webhook_requests_handler.register(app, path=config.WEBHOOK_PATH)

    setup_application(app, dp, on_startup=on_startup, on_shutdown=on_shutdown)
    return app


if __name__ == "__main__":
    import asyncio
    from aiohttp import web

    app = asyncio.run(create_app())
    web.run_app(app, port=8000)
