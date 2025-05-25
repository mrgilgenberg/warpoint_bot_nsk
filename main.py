from app.config import settings
from app.utils import setup_logger, logger
from app.logic import setup_default_commands, ThrottlingMiddleware
from app.load import dp
from app.handlers import load_handlers

from aiogram import Dispatcher
from aiogram.utils import executor

from bot_sources import init_bot_sources

async def on_startup(dispatcher: Dispatcher):
    load_handlers(['commands', 'callbacks', 'states'])
    dispatcher.setup_middleware(ThrottlingMiddleware(dispatcher=dp))
    await setup_default_commands(dispatcher)


if __name__ == '__main__':
    init_bot_sources()
    setup_logger(path=settings.LOG_PATH, name=settings.LOG_NAME, level=settings.LOG_LEVEL)
    logger.info(f'Bot Started')
    executor.start_polling(
        dp, on_startup=on_startup
    )

