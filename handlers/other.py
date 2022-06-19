from aiogram import types, Dispatcher
import json, string
from aiogram.dispatcher.filters import Text

async def profanity(message : types.Message):
    if {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('profanity\cenz.json')))) != set():
        await message.reply('Ненормативная лексика запрещена')
        await message.delete()   #ГЕНЕРАТОР МНОЖЕСТВА ДЛЯ ИСКЛЮЧЕНИЯ МАТА

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(profanity)
    
