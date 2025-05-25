from app.utils import logger

from aiogram.dispatcher.filters import Filter
from aiogram.types import CallbackQuery


class CallDataEqualFilter(Filter):
    def __init__(self, call_data: str):
        self.call_data = call_data

    async def check(self, obj: CallbackQuery):
        if not isinstance(obj, CallbackQuery):
            logger.warning(f'{self.__class__.__name__} does not support {type(obj)} as input')
            return False

        return obj.data == self.call_data
