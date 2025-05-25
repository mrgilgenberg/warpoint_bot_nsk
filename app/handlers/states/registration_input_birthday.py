import logging
import re
from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import ChatType, Message

from app.load import dp, bot
from app.logic.states import  Registration
from app.logic.filters import RegisteredUserFilter
from app.database import BotDB
from bot_sources import bot_answers

from app.logic.keyboards.inline import CheckSubstInlineKeyboard


@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE),
                    RegisteredUserFilter(bot_db=BotDB),
                    state=Registration.input_birthday)
async def state_registration_input_partner_id(message: Message, state: FSMContext):
    try:
        if not re.match(r'^(0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[0-2]).(\d{4})$', message.text):
            return await message.answer(
                text=bot_answers.error_input_d_birth_format,
            )
        try:
            birthday_date = datetime.strptime(message.text, '%d.%m.%Y').date()
        except Exception:
            return await message.answer(
                text=bot_answers.error_input_d_birth_format,
            )

        await BotDB.update_user(
            n_telegram_id=message.from_id,
            key='d_birthday',
            value=birthday_date.strftime('%Y-%m-%d')
        )
        # try:
        #     await message.delete()
        #     await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        # except Exception:
        #     pass

        await state.finish()
        await message.answer(
            text=bot_answers.callback_input_d_birth,
        )
        # start check subs
        await message.answer(
            text=bot_answers.start_check_subs,
            reply_markup=CheckSubstInlineKeyboard()
        )

    except Exception as e:
        logging.error(e)
