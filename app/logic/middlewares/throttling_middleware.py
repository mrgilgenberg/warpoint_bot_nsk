from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.utils.exceptions import Throttled
from aiogram import Dispatcher



class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self,
                 dispatcher: Dispatcher,
                 message_rate_limit: float = 0.8,
                 callback_query_rate_limit: float = 0.4):
        BaseMiddleware.__init__(self)
        self.message_rate_limit = message_rate_limit
        self.callback_query_rate_limit = callback_query_rate_limit
        self.dispatcher = dispatcher

    async def on_process_message(self, message: Message, date: dict):
        try:
            await self.dispatcher.throttle(key='antiflood_message', rate=self.message_rate_limit)
        except Throttled:
            raise CancelHandler()

    async def on_process_callback_query(self, call: CallbackQuery, date: dict):
        try:
            await self.dispatcher.throttle(key='antiflood_callback_query', rate=self.callback_query_rate_limit)
        except Throttled:
            raise CancelHandler()
