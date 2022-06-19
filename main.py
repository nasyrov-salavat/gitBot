from aiogram.utils import executor
from pathlib import Path
 


# outpath = Path.cwd() / 'handlers' / 'client.py'
# print(outpath)
 



import handlers.client as client
import handlers.other as other

from handlers.client import dp
from data_base import sqlite_db

async def on_startup(_):
    print('Бот онлайн')
    sqlite_db.sql_start()

client.register_handlers_client(dp)
client.register_handlers_callback(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)