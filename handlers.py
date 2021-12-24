from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from main import dp
from sql import add, buy

@dp.message_handler(Command('add'))
async def add_cmd(message: Message):
    s = ' '.join(message.text.split(' ')[1:])
    await add(s)
    await message.answer('Запсиь успешно добавлена!!!')

@dp.message_handler(Command('buy'))
async def buy_cmd(message: Message):
    await message.answer(await buy())