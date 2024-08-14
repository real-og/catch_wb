import asyncio
from aiogram import Bot
import requests
import json
import os

BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ID = str(os.environ.get("ID"))

bot = Bot(BOT_TOKEN, parse_mode='HTML')


async def async_send_message(text):
    try:
        mes = await bot.send_message(ID, text)
        s = await bot.get_session()
        await s.close()
        return mes.message_id
    except Exception as e:
        print(e)



def send_text_message(text):
    message_id = asyncio.run(async_send_message(text))
    return message_id