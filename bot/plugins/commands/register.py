import asyncio

from ...core import client
from ...core import client 
from ...core.logger import log
from ...database.redis import antidb 
from bot import mdb
import time
import datetime
log.info("Register command activated")

from telethon import events

async def reg(m):
    user_info = await mdb.find_one('main', {'_id': m.sender_id})
    if not user_info:
        

        x = datetime.datetime.now()

        y = x.strftime("%d-%m-%Y")

        upload = {
            '_id': m.sender_id,
            'type': 'F',
            'role': 'Free User',
            'date_registered': y,
            
        }
        x = await mdb.insert_one('main', upload)
        if x:
            user_info = await mdb.find_one('main', {'_id': m.sender_id})
            if user_info:
                return user_info
        return False
    return user_info
# @client.on(events.NewMessage(pattern=r"\/register"))
# async def register(event):
#     msg = await event.reply("Fetching")
#     user_info = await mdb.find_one('main', {'_id': event.sender_id})
#     if not user_info:
#         upload = {
#             '_id': event.sender_id,
#             'type': 'F',
#             'role': 'Free',
#             'credits': 0,
#             'antispam': True,
#             'antispam_time': 60,
#             'saveccs': True,
#             'keys': [],
#             'claimed_date': [],
#             'lives': [],
#         }
#         x = await mdb.insert_one('main', upload)
#         if x:
#             user_info = await mdb.find_one('main', {'_id': event.sender_id})
#             if user_info:
#                 await msg.edit(f"""
# Registration Successful!
# """,parse_mode="HTML")
#                 return user_info
#         return False
#     await msg.edit(f"""
# Sorry you are already registerd
# """,parse_mode="HTML")

#     return user_info

    