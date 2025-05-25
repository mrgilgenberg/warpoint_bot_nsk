import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import ChatType, Message, ContentTypes, ReplyKeyboardRemove

from app.load import dp, bot
from app.logic.states import  Registration
from app.logic.filters import RegisteredUserFilter
from app.database import BotDB
from bot_sources import bot_answers


def get_phone(text: str) -> str:
    phone = ''
    for char in text:
        if char.isdigit():
            phone += char
    return phone


@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE),
                    RegisteredUserFilter(bot_db=BotDB),
                    content_types=ContentTypes.CONTACT,
                    state=Registration.input_phone)
async def state_registration_input_phone(message: Message, state: FSMContext):
    try:
        vc_phone = get_phone(message.contact.phone_number)
        await BotDB.update_user(
            n_telegram_id=message.from_id,
            key='vc_phone',
            value=vc_phone[:11]
        )
        await message.answer(
            text=bot_answers.callback_input_phone,
            reply_markup=ReplyKeyboardRemove()
        )
        await state.finish()
        # try:
        #     await message.delete()
        #     await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        # except Exception:
        #     pass

        # start input b_date
        await Registration.input_birthday.set()
        await message.answer(
            text=bot_answers.start_input_d_birth,
        )
    except Exception as e:
        logging.error(e)



