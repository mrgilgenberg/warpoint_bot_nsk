from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app.config import settings

bot = Bot(token=settings.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot=bot, storage=storage)

__all__ = [
    'bot',
    'storage',
    'dp'
]
