from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


class PhoneReplyKeyboard(ReplyKeyboardMarkup):
    def __init__(self):
        super().__init__(resize_keyboard=True)

        self.add(
            KeyboardButton(
                text='Отправить номер 📱',
                request_contact=True
            )
        )
