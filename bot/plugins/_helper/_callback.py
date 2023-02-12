from ...core import client
from telethon.events import CallbackQuery
import logging
from ...core.logger import log 
def callback(data=None, from_users=[], owner=False, **kwargs):
    """Assaist callback decoretor made by ani"""
    if "me" in from_users:
        from_users.remove("me")
        from_users.append(client.botid)

    def ultr(func):
        async def wrapper(event):
            m = await event.get_message()
            rm = await m.get_reply_message()
            if not owner and  event.sender_id != rm.sender_id:
                return await event.answer("You dont have permission on this butons.", alert=True)
            if from_users and event.sender_id not in from_users:
                return await event.answer("Not for You! Make for your if you need.", alert=True)
            elif owner and event.sender_id != 5640958137:
                return await event.answer(f"This Function Is Only For Owner", alert = True)
            try:
                await func(event)
            except Exception as er:
                log.exception(er)

        client.add_event_handler(wrapper, CallbackQuery(pattern=data, **kwargs))

    return ultr