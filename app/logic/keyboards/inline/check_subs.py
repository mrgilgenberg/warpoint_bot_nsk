from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton


class CheckSubstInlineKeyboard(InlineKeyboardMarkup):
    def __init__(self, row_width: int = 1):
        super().__init__(row_width)

        self.add(
            InlineKeyboardButton(
                text='WARPOINT | Новосибирск',
                url='https://t.me/WARPOINTNSK'
            ),
            InlineKeyboardButton(
                text='Я подписался ✅',
                callback_data='check_subs_to_channel'
            )
        )