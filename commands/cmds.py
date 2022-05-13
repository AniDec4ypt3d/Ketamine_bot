import asyncio
from ..core import tgbot , client
from ..database.redis import antidb
import time
print("cmds started")

from telethon import events
@tgbot.on(events.NewMessage(pattern=r"\/cmds"))
async def _(event):
    msg = await event.reply("Fetching")
    await msg.edit(f"""
<b>XTRA 2.1 | TELETHON XD</b>

soon
""",parse_mode="HTML")
