import os,sys
import re
from ....core.adb import adb
from time import gmtime, strftime
from veriable.veriable import LOG_CHAT
from ..decoretors import msg_send

@msg_send(cmd="auth", admins_only = True, group_only = True)
async def _(m):
    if await adb.get_key(f'approved_{str(m.chat_id)}'):
        return await m.reply("<b>๐๐ซ๐จ๐ฎ๐ฉ ๐๐ฅ๐ซ๐๐๐๐ฒ ๐๐ฎ๐ญ๐ก๐จ๐ซ๐ข๐ณ๐๐</b>")
    test = await adb.set_key(f'approved_{str(m.chat_id)}', m.chat_id)
    if test:
        await m.reply("<b>๐ฎ๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐๐๐</b>")
    else:
        await m.reply("<b>Error de excepciรณn</b>")




@msg_send(cmd="unauth", admins_only = True, group_only = True)
async def _(m):
    if not await adb.get_key(f'approved_{str(m.chat_id)}'):
        return await m.sod("๐๐ซ๐จ๐ฎ๐ฉ ๐ง๐จ๐ญ ๐๐จ๐ฎ๐ง๐")
    test = await adb.del_key(f'approved_{str(m.chat_id)}')
    if test:
        await m.sod("๐ฎ๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐๐๐", time = 5)
    else: await m.sod(f"Error de excepciรณn", time = 5)
