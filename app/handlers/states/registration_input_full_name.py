from app.utils import logger

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import ChatType, Message

from app.load import dp, bot
from app.logic.states import  Registration
from app.logic.filters import RegisteredUserFilter
from app.database import BotDB
from bot_sources import bot_answers

from app.logic.keyboards.reply import PhoneReplyKeyboard


@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE),
                    RegisteredUserFilter(bot_db=BotDB),
                    state=Registration.input_full_name)
async def state_input_full_name(message: Message, state: FSMContext):
    try:
        # try:
        #     await message.delete()
        #     await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        # except Exception:
        #     pass
        vc_full_name = message.text[:128]
        await BotDB.update_user(
            n_telegram_id=message.from_id,
            key='vc_full_name',
            value=vc_full_name
        )
        await state.finish()
        await message.answer(f'{bot_answers.callback_input_full_name}, {vc_full_name}')
        # start input phone
        await Registration.input_phone.set()
        await message.answer(
            text=bot_answers.start_input_phone,
            reply_markup=PhoneReplyKeyboard()
        )
    except Exception as e:
        logger.error(e)
