from app.utils import logger

from aiogram.dispatcher.filters import Filter
from aiogram.types import CallbackQuery, Message


class RegisteredUserFilter(Filter):
    def __init__(self, bot_db):
        self.bot_db = bot_db

    async def check(self, obj: CallbackQuery):
        if isinstance(obj, CallbackQuery):
            n_telegram_id = obj.from_user.id
        elif isinstance(obj, Message):
            n_telegram_id = obj.from_id
        else:
            logger.warning(f'{self.__class__.__name__} does not support {type(obj)} as input')
            return False

        user = await self.bot_db.get_user(
            n_telegram_id=n_telegram_id
        )

        return user is not None
