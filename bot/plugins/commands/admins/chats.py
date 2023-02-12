import os,sys
import re
from ....core.adb import adb
from time import gmtime, strftime
from veriable.veriable import LOG_CHAT
from ..decoretors import msg_send

@msg_send(cmd="auth", admins_only = True, group_only = True)
async def _(m):
    if await adb.get_key(f'approved_{str(m.chat_id)}'):
        return await m.reply("<b>𝐆𝐫𝐨𝐮𝐩 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝</b>")
    test = await adb.set_key(f'approved_{str(m.chat_id)}', m.chat_id)
    if test:
        await m.reply("<b>𝑮𝒓𝒐𝒖𝒑 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒂𝒕𝒊𝒐𝒏 𝒔𝒖𝒄𝒄𝒆𝒔𝒔</b>")
    else:
        await m.reply("<b>Error de excepción</b>")




@msg_send(cmd="unauth", admins_only = True, group_only = True)
async def _(m):
    if not await adb.get_key(f'approved_{str(m.chat_id)}'):
        return await m.sod("𝐆𝐫𝐨𝐮𝐩 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝")
    test = await adb.del_key(f'approved_{str(m.chat_id)}')
    if test:
        await m.sod("𝑮𝒓𝒐𝒖𝒑 𝒖𝒏𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒂𝒕𝒊𝒐𝒏 𝒔𝒖𝒄𝒄𝒆𝒔𝒔", time = 5)
    else: await m.sod(f"Error de excepción", time = 5)
