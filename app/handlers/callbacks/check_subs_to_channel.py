from app.utils import logger

from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import ChatType, CallbackQuery

from app.load import dp, bot
from app.logic.filters import RegisteredUserFilter, CallDataEqualFilter
from app.database import BotDB
from bot_sources import bot_answers, bot_content


async def check_in_channel(channel, user):
    result_check = await bot.get_chat_member(chat_id=channel, user_id=user)
    logger.debug('''!!!check_in_channel !!!''')
    logger.debug(result_check)
    logger.debug('''!!!check_in_channel !!!''')
    return result_check


@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE),
                           CallDataEqualFilter('check_subs_to_channel'),
                           RegisteredUserFilter(bot_db=BotDB))
async def call_get_cert(call: CallbackQuery):
    try:
        result_check = await check_in_channel(channel='@WARPOINTNSK', user=call.message.chat.id)
        if result_check.status == 'left':
            await call.answer(text=bot, show_alert=True)
        else:
            await call.message.edit_reply_markup()
            await call.message.answer_photo(
                photo=bot_content.cert_file_id,
                caption=bot_answers.caption_cert
            )
    except Exception as e:
        logger.error(e)
