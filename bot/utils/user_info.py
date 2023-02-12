
from time import strftime, gmtime

import datetime
from bot import mdb



async def user_info(m):
    """get user info from server."""
    user_info = await mdb.find_one('main', {'_id': m.sender_id})
    if not user_info:
        sender = await m.get_sender()
        x = datetime.datetime.now()

        y = x.strftime("%d-%m-%Y")

        upload = {
            '_id': m.sender_id,
            'type': 'F',
            'role': 'Free User',
            'date_registered': y,
        }
        x = await mdb.insert_one('main', upload)
        if x :
            user_info = await mdb.find_one('main', {'_id': m.sender_id})
            if user_info:
                return user_info
        return False
    return user_info



def get_user_info():
    """get user info."""
    def strings(func):
        async def wrap(*args, **kwargs):
            m = args[0]
            _ = await user_info(m)
            if _:
                await func(*args,_, **kwargs)
            else:
                await m.reply("Error While Getting User Info")
                return
        return wrap
    return strings
