from bot import mdb
from ...core import client 
from telethon import Button 
from ...utils.user_info import get_user_info
from .._helper._callback import callback
from ...core.logger import log
log.info("Cmds imported")



from telethon import events
@client.on(events.NewMessage(pattern=r"\/cmds"))

@get_user_info()    
async def _(m , user_db):
    role = user_db['role']
    if role == 'Free User'  and  m.is_private:
        return await m.reply("Unauthorized user detected")
    elif role == 'Free User' and not m.is_private:
        pass
    elif role == 'Owner':
        pass
    nu = [
    [
        Button.inline("𝑭𝒓𝒆𝒆 𝑮𝒂𝒕𝒆𝒔","p1"),
        Button.inline("𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑮𝒂𝒕𝒆𝒔","p2"),
    ],    [
        Button.inline("𝑴𝒚 𝒊𝒏𝒇𝒐","p3"),
        Button.inline("𝑨𝒃𝒐𝒖𝒕 𝑩𝒐𝒕","p4"),
    ],
]
    await m.reply("𝑪𝒉𝒆𝒄𝒌 𝒎𝒚 𝒑𝒍𝒖𝒈𝒊𝒏𝒔",buttons=nu),