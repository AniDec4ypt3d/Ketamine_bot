import asyncio

from ..core import tgbot
from ..database.redis import antidb
import time
from ..checkers import stripe_chk

print("import handler")


@tgbot.on_cmd("chk")
async def _(event):
    antispam_time = int(antidb.get(event.sender_id).decode("utf-8"))
    spam_time = int(time.time()) - antispam_time
    if spam_time < 60:
        time_left = 60 - spam_time
        await event.reply(f"<b> AntiSpam try again after {time_left}'s</b>",parse_mode="HTML")
    else:
        msg = await event.reply("`Checking....`")
        antidb.set(event.sender_id, int(time.time()))
        await asyncio.sleep(5)
        result = stripe_chk.check(event.ccn, event.month, event.year, event.cvc)

        await msg.edit(
f"""**Card:** `{event.card}`
**Result:** `{result}`"""
        )
