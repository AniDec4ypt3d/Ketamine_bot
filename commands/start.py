import asyncio
from ..core import tgbot
import time
print("cmds started")

from telethon import events
@tgbot.on(events.NewMessage(pattern=r"\/start"))
async def _(event):
    msg = await event.reply("Starting")
    await msg.edit(f"""
<i>Hey!! how are you? Hope you are doing well. 
I am a checker bot</i>
<b>Powered -> TeleThon
Language -> Python</b>
<b>Developed by -> AniDec4ypt3d and Sujeet</b>
""",parse_mode="HTML")
