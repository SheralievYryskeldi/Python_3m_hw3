from aiogram import executor
from bot_instance import dp
from handlers import fsdamin

fsdamin.register_handler_fsadmin(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)