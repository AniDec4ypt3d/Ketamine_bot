import asyncio
from ....core import client 
from ....core.logger import log
from ....database.redis import antidb 
from bot import mdb
import time
from veriable.veriable import LOG_CHAT
import datetime
log.info("Direct promote commands activated")

from telethon import events
import re

@client.on(events.NewMessage(pattern=r"\/pr")) 
async def promote(m):
    reply = await m.get_reply_message()
    pram = m.text.split(' ', maxsplit=1)[1]
    sender = await m.get_sender()
    # print(pram)
    pram = int(pram)
    filter = {'_id': pram}

    data = {'$set': {
            'type': 'P',
            'role': 'Premium User',
        }}
    a = await mdb.update_one('main',filter, data)
    if a:
        await m.reply("PREMIUM SUCCESS")
        await m.client.send_message(LOG_CHAT,  f"{pram} is premium now by {sender.username}")
  