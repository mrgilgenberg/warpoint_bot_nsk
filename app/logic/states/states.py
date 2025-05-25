from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration(StatesGroup):
    input_full_name = State()
    input_birthday = State()
    check_subs = State()
    input_phone = State()


ALL_STATES = (
    Registration.input_full_name,
    Registration.input_birthday,
    Registration.check_subs,
    Registration.input_phone
)

