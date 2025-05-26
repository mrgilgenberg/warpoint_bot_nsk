from app.utils import logger

from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ChatType, Message

from app.load import dp
from app.logic.states import ALL_STATES, Registration

from app.logic.filters import RegisteredUserFilter, UnregisteredUserFilter
from bot_sources import bot_answers, bot_content
from app.database import BotDB
import traceback


@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE),
                    RegisteredUserFilter(bot_db=BotDB),
                    commands=['start'],
                    state=(*ALL_STATES, None))
async def start_registered(message: Message, state: FSMContext):
    try:
        await state.finish()

        user = await BotDB.get_user(
            n_telegram_id=message.from_id
        )
        await message.delete()

        if user.d_birthday:
            await message.answer(
                text=f'{user.vc_full_name} {bot_answers.start_registered}'
            )
        else:
            await Registration.input_full_name.set()

            await message.answer_photo(
                photo=bot_content.first_message_photo_file_id,
                caption=bot_answers.start_input_full_name
            )
    except Exception as e:
        logger.error(traceback.format_exc())


@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE),
                    UnregisteredUserFilter(bot_db=BotDB),
                    commands=['start'],
                    state=(*ALL_STATES, None))
async def start_unregistered(message: Message):
    try:

        message_list = message.text.split(' ')
        n_presenter_id = 0
        if len(message_list) == 2:
            n_presenter_id = int(message_list[1])

        presenter = await BotDB.get_presenter(
            n_presenter_id=n_presenter_id
        )
        await Registration.input_full_name.set()
        await BotDB.post_user(
            n_telegram_id=message.from_id,
            uu_presenter_id=presenter.uu_presenter_id
        )
        await message.answer_photo(
            photo=bot_content.first_message_photo_file_id,
            caption=bot_answers.start_input_full_name
        )
    except Exception as e:
        logger.error(traceback.format_exc())
