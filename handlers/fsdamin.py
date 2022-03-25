from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot_instance import dp, bot

class FSMADMIN(StatesGroup):
    id = State()
    username = State()
    first_name = State()
    last_name = State()

async def is_admin_func(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Admin, What do u need")

async def fsm_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await FSMADMIN.id.set()
        await message.reply("Admin, Send me id please")

async def load_username(message: types.Message,
                        state: FSMContext):
    # if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["username"] = message.text
        await FSMADMIN.next()
        await message.reply("Send me username")

async def load_first_name(message: types.Message,
                          state: FSMContext):
    # if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["first_name"] = message.text
        await FSMADMIN.next()
        await message.reply("Send me user's first name")

async def load_last_name(message: types.Message,
                         state: FSMContext):
    # if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["last_name"] = message.text
        await FSMADMIN.next()
        await message.reply("Send me user's last_name")

def register_handler_fsadmin(dp: Dispatcher):
    dp.register_message_handler(is_admin_func, commands=['admin'], is_chat_admin=True)
    dp.register_message_handler(fsm_start, commands=['id'], state=None)
    dp.register_message_handler(load_username, state=FSMADMIN.username)
    dp.register_message_handler(load_first_name, state=FSMADMIN.first_name)
    dp.register_message_handler(load_last_name, state=FSMADMIN.last_name)