# """
# ≛ <b>Commands Available</b> ≛
# ──────────────────────
# - <code>/add_auth</code>: Add new auth gate if not exists.
# ➻ Example: <code>/add_auth chk Stripe </code>
# ──────────────────────
# - <code>/add_charge</code>: Add new charge gate if not exists.
# ➻ Example: <code>/add_charge chk Stripe 5</code>
# ──────────────────────
# - <code>/add_other</code>: Add new other gate if not exists.
# ➻ Example: <code>/add_other chk Stripe</code>
# ──────────────────────
# <code>/del_gate</code>: Delete the gate if exists.
# ➛ param: <b>Command name</b>
# ➻ Example: <code>/del_gate chk<code>
# ──────────────────────
# <code>/cha_gate</code>: Change the gate type to paid or free if gate is paid else free to paid.
# ➛ param: <b>Command name</b>
# ➻ Example: <code>/cha_gate chk<code>
# ──────────────────────
# <code>/open_gate</code>: Open gate if closed.
# ➛ param: <b>Command name</b>
# ➻ Example: <code>/cha_gate chk<code>
# ──────────────────────
# <code>/list_gate<code>: List of all gates added in bot
# ➻ Example: <code>/list_gate<code>
# ──────────────────────
# ©<a href="https://t.me/roldexverse">RoldexVerse</a>
# """


import os,sys
import re
from bot import mdb
from time import gmtime, strftime
from veriable.veriable import LOG_CHAT
from ..decoretors import msg_send



@msg_send(cmd="add_auth", admins_only = True)
async def _(m):
    params = m.pattern_match.group(1).strip().split(maxsplit=1)
    if len(params) < 2:
        await m.reply("Wrong Input Check Example: <code>/add_auth cmd_name gate_name</code>")
        return
    is_gate = await mdb.find_one('gate',  params[0].lower())
    if is_gate:
        await m.reply("Gate Already Exists")
        return
    gate_dict = {
        '_id': params[0].lower(),
        'status': True,
        'status_logo': 'ON ✅',
        'gate_type': 'auth',
        'cmd_name': params[0],
        'gate_name': params[1].title(),
        'made_by_id': m.sender_id,
        'made_by_name': m.full_name(),
        'is_paid': False,
        'comment': 'No comment added',
        'date': strftime("%Y-%m-%d", gmtime())
    }
    insert = await mdb.insert_one('gate',  gate_dict)
    if insert:
        await m.client.send_message(LOG_CHAT,  f"Gate Added: <code>{params[0]}</code> with name <code>{params[1]}</code> by <a href='tg://user?id={m.sender_id}'>{m.full_name()}</a>")
        await m.reply("Gate Added Successfully")
    else:
        await m.reply("Error While Adding Gate")




@msg_send(cmd="add_charge", admins_only = True)
async def _(m):
    params = m.pattern_match.group(1).strip().split(maxsplit=1)
    if len(params) < 2:
        await m.reply("Wrong Input Check Example: <code>/add_charge cmd_name gate_name charge_amount</code>")
        return
    is_gate = await mdb.find_one('gate',  params[0].lower())
    if is_gate:
        await m.reply("Gate Already Exists")
        return
    dig = re.findall('\d+', params[1])
    amount_name = dig[-1] if dig else None
    if not amount_name:
        return await m.reply("Wrong Input Check Example: <code>/add_charge cmd_name gate_name charge_amount</code>")
    gate_name = params[1].replace(amount_name, '').strip().title()
    gate_dict = {
    '_id': params[0].lower(),
    'status': True,
    'status_logo': 'ON ✅',
    'gate_type': 'charge',
    'charge_amount': amount_name,
    'cmd_name': params[0],
    'gate_name': gate_name,
    'made_by_id': m.sender_id,
    'made_by_name': m.full_name(),
    'is_paid': True,
    'comment': 'No comment added',
    'date': strftime("%Y-%m-%d", gmtime())
    }
    insert = await mdb.insert_one('gate',  gate_dict)
    if insert:
        await m.client.send_message(LOG_CHAT,  f"Gate Added: <code>{params[0]}</code> with name <code>{params[1]}</code> by <a href='tg://user?id={m.sender_id}'>{m.full_name()}</a>")
        await m.reply("Gate Added Successfully")
    else:
        await m.reply("Error While Adding Gate")




@msg_send(cmd="add_other", admins_only = True)
async def _(m):
    params = m.pattern_match.group(1).strip().split(maxsplit=1)
    if len(params) < 2:
        await m.reply("Wrong Input Check Example: <code>/add_other cmd_name gate_name</code>")
        return
    is_gate = await mdb.find_one('gate',  params[0].lower())
    if is_gate:
        await m.reply("Gate Already Exists")
        return
    gate_dict = {
        '_id': params[0].lower(),
        'status': True,
        'status_logo': 'ON ✅',
        'gate_type': 'other',
        'cmd_name': params[0],
        'gate_name': params[1].title(),
        'made_by_id': m.sender_id,
        'made_by_name': m.full_name(),
        'is_paid': True,
        'date': strftime("%Y-%m-%d", gmtime())
    }
    insert = await mdb.insert_one('gate',  gate_dict)
    if insert:
        await m.client.send_message(LOG_CHAT,  f"Gate Added: <code>{params[0]}</code> with name <code>{params[1]}</code> by <a href='tg://user?id={m.sender_id}'>{m.full_name()}</a>")
        await m.reply("Gate Added Successfully")
    else:
        await m.reply("Error While Adding Gate")




@msg_send(cmd="add_mass", admins_only = True)
async def _(m):
    params = m.pattern_match.group(1).strip().split(maxsplit=1)
    if len(params) < 2:
        await m.reply("Wrong Input Check Example: <code>/add_mass cmd_name gate_name</code>")
        return
    is_gate = await mdb.find_one('gate',  params[0].lower())
    if is_gate:
        await m.reply("Gate Already Exists")
        return
    gate_dict = {
        '_id': params[0].lower(),
        'status': True,
        'status_logo': 'ON ✅',
        'gate_type': 'mass',
        'cmd_name': params[0],
        'gate_name': params[1].title(),
        'made_by_id': m.sender_id,
        'made_by_name': m.full_name(),
        'is_paid': True,
        'date': strftime("%Y-%m-%d", gmtime())
    }
    insert = await mdb.insert_one('gate',  gate_dict)
    if insert:
        await m.client.send_message(LOG_CHAT,  f"Gate Added: <code>{params[0]}</code> with name <code>{params[1]}</code> by <a href='tg://user?id={m.sender_id}'>{m.full_name()}</a>")
        await m.reply("Gate Added Successfully")
    else:
        await m.reply("Error While Adding Gate")





@msg_send(cmd="del_gate", admins_only = True)
async def _(m):
    params = m.pattern_match.group(1).strip().split()
    if len(params) < 1 or not params[0].isalpha():
        await m.reply("Wrong Input Check Example: <code>/del_gate cmd_name</code>")
        return
    is_gate = await mdb.find_one('gate',  params[0].lower())
    if not is_gate:
        await m.reply("Gate Doesn't Exists")
        return
    insert = await mdb.delete('gate', {'_id': params[0].lower()})
    if insert:
        await m.client.send_message(LOG_CHAT,  f"Gate Removed: <code>{params[0]}</code> by <a href='tg://user?id={m.sender_id}'>{m.full_name()}</a>")
        await m.reply("Gate Removed Successfully")
    else:
        await m.reply("Error While Removing Gate")




@msg_send(cmd="cha_gate", admins_only = True)
async def _(m):
    params = m.pattern_match.group(1).strip().split()
    if len(params) < 1 or not params[0].isalpha() :
        await m.reply("Wrong Input Check Example: <code>/cha_gate cmd_name</code>")
        return
    is_gate = await mdb.find_one('gate',  params[0].lower())
    if not is_gate:
        await m.reply("Gate Doesn't Exists")
        return
    update = await mdb.update_one('gate', {'_id': params[0].lower()}, {'$set': {'is_paid': True if not is_gate['is_paid'] else False}})
    if update:
        await m.client.send_message(LOG_CHAT,  f"Gate Updated: <code>{params[0]}</code> with <code>{True if not is_gate['is_paid'] else False}</code>  by <a href='tg://user?id={m.sender_id}'>{m.full_name()}</a>")
        await m.reply("Gate Updated Successfully")
    else:
        await m.reply("Error While Removing Gate")




@msg_send(cmd="down_gate", admins_only = True)
async def _(m):
    # params = m.pattern_match.group(1).strip().split()
    params = m.pattern_match.group(1).strip().split(maxsplit=1)
    if len(params) < 1 or not params[0].isalpha() :
        await m.reply("Wrong Input Check Example: <code>/down_gate cmd_name</code>")
        return
    is_gate = await mdb.find_one('gate',  params[0].lower())
    if not is_gate:
        await m.reply("Gate Doesn't Exists")
        return
    update = await mdb.update_one('gate', {'_id': params[0].lower()}, {
            '$set': {'status_logo': 'OFF ❌','status': False,'comment': params[1].title()}
            })            
    if update:
        await m.client.send_message(LOG_CHAT,  f"Gate Updated: <code>{params[0]}</code> with <code>{True if not is_gate['status'] else False}</code> by <a href='tg://user?id={m.sender_id}'>{m.full_name()}</a> ")
        await m.reply("Gate Updated Successfully")
    else:
        await m.reply("Error While Removing Gate")

@msg_send(cmd="open_gate", admins_only = True)
async def _(m):
    params = m.pattern_match.group(1).strip().split()
    if len(params) < 1 or not params[0].isalpha() :
        await m.reply("Wrong Input Check Example: <code>/open_gate cmd_name</code>")
        return
    is_gate = await mdb.find_one('gate',  params[0].lower())
    if not is_gate:
        await m.reply("Gate Doesn't Exists")
        return
    update = await mdb.update_one('gate', {'_id': params[0].lower()}, {
            '$set': {'status_logo': 'ON ✅','status': True,'comment':'No comment added'}
            })            
    if update:
        await m.client.send_message(LOG_CHAT,  f"Gate Updated: <code>{params[0]}</code> with <code>{True if not is_gate['status'] else False}</code> by <a href='tg://user?id={m.sender_id}'>{m.full_name()}</a> ")
        await m.reply("Gate Updated Successfully")
    else:
        await m.reply("Error While Removing Gate")


@msg_send(cmd="list_gate", admins_only = True)
async def _(m):
    count = await mdb.get_count('gate')
    await m.reply("I got a count of {} gates".format(count))
