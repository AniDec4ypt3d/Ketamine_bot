import asyncio
from ...core import client 
from .decoretors import msg_send
from ...core.logger import log
from ...utils.user_info import get_user_info
import time
from bot import mdb
log.info("Start message imported")

from telethon import events

@msg_send(cmd="start", admins_only = False)
@get_user_info()    
async def _(m , user_db):
    # role = user_db['role']
    # if role == 'Free User'  and  m.is_private:return await m.reply("Unauthorized user detected")
    # elif role == 'Free User' and not m.is_private:pass
    # elif role == 'Owner':pass
    out = "https://xtrachkbot.alwaysdata.net/xtrachkbot/akeno.jpg"
    msg = await m.reply("Starting",file = out)
    await msg.edit(f"""
𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 - 𝗯𝗼𝘁, 𝗰𝗵𝗲𝗰𝗸 /cmds 𝗳𝗼𝗿 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀.
""",parse_mode="HTML")
