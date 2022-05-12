import asyncio

from ..core import tgbot


@tgbot.on_cmd("cmds")
async def _(event):
    msg = await event.reply("Collections coming")
    asyncio.sleep(2)
    await msg.edit(f"""
<b>XTRA CMDS | TELETHON PWD</b>

Coming af
""",parse_mode="HTML")
