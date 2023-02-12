


import os,sys
import random
from time import gmtime, strftime
import time

from veriable.veriable import LOG_CHAT
from ..decoretors import msg_send
from ....utils  import user_info
from ....core.logger import log
from bot import mdb


@msg_send(cmd="key", admins_only = True)
async def _(m):
    params = m.pattern_match.group(1).strip()
    if len(params) == 0 or params != 'test' and not params.isdigit():
        await m.sod("Wrong Input Check Example: <code>/gkey days[int] | test</code>", time = 5)
        return
    data = int(params) if params.isdigit() else 1
    type = 'hour' if params == 'test' else 'day'
    rand_digit = random.random_integer()
    rand_string = random.random_string(5)
    key = f"KEY-{rand_digit}-{rand_string}-PREMIUM"
    add = {
        '_id': key,
        'data': data,
        'time_type': type,
        'gen_by': m.sender_id,
        'gen_name': m.full_name(),
        'gen_date': strftime("%Y-%m-%d", gmtime()),
        'type': 'P',
    }
    insert = await mdb.insert_one('keys',  add)
    if insert:
        log.info(f"{m.sender_id} Generated Key: {key}")
        text = f"""
<code>╾╾╾╾╾╾╾╾╾ [ 𝑲𝒆𝒚 𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒐𝒓 ] ╾╾╾╾╾╾╾╾╾</code>
<b>⎈ 𝑪𝒐𝒅𝒆 ⪢</b> <code>{key}</code>
<b>⎈ 𝑷𝒆𝒓𝒊𝒐𝒅 ⪢</b> <code>{data} days</code>
<b>⎈ _𝑩𝒚 ⪢</b> <code>{m.full_name()}</code>
<b>⎈ _𝑶𝒏 ⪢</b> <code>{strftime("%Y-%m-%d", gmtime())}</code>
"""
        await m.reply(text,parse_mode="HTML")
        await m.client.send_message(LOG_CHAT,  f"{m.sender_id} Generated Key: {key}")
    else:
        await m.sod("Error While Generating Key", time = 5)



@msg_send(cmd="dkey", admins_only = True)
async def _(m):
    params = m.pattern_match.group(1).strip()
    if not params or not ( params.startswith('MILLIE-') and params.endswith('PREMIUM') ):
        await m.sod("Wrong Input Check Example: <code>/dkey key</code>", time = 5)
        return
    is_key = await mdb.find_one('keys', {'_id': params})
    if not is_key:
        await m.sod("Provided key not found Example: <code>/gkey key</code>", time = 5)
        return
    log.info(f"{m.sender_id} Deleted Key: {params}")
    await m.sod(f"`{params}` key deleted from server.")

