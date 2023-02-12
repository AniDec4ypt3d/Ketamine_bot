from .._callback import callback
from telethon import Button
import pymongo
from bot import mdb , sdb
from ..local import send_main


@callback(data="p1", owner=False)
async def _(m):

    finded = sdb['gate'].find({'gate_type': 'auth'}, {'_id':0, 'cmd_name': 1 , 'status_logo': 1, 'gate_name': 1, 'is_paid': 1,'comment': 1}).sort("abc",pymongo.DESCENDING)
    finded = list(finded)
    len_find = len(finded)
    text = f"<b>⎈ 𝑻𝒐𝒕𝒂𝒍 𝑮𝒂𝒕𝒆𝒘𝒂𝒚𝒔 ⪢</b> <code>{len_find}</code>\n"
    for a in finded:
        text += f"""
╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾
<b>⎈ {a['gate_name']} ⪢</b> <code>/{a['cmd_name']} cc|mm|yy|cv</code>
<b>⎈ 𝑺𝒕𝒂𝒕𝒖𝒔 ⪢</b> <code>{a['status_logo']}</code>
<b>⎈ 𝑪𝒐𝒎𝒎𝒆𝒏𝒕 ⪢</b> <code>{a['comment']}</code>
"""
    nu = [
    [
        Button.inline("Previous","home"),
        # Button.inline("Next","free1"),
    ]
]
    await m.edit(text,parse_mode= 'HTML', buttons = nu)


@callback(data="p2", owner=False)
async def _(m):
    finded = sdb['gate'].find({'gate_type': 'charge'}, {'_id':0, 'cmd_name': 1 , 'status_logo': 1, 'gate_name': 1, 'is_paid': 1,'comment': 1}).sort("abc",pymongo.DESCENDING)
    finded = list(finded)
    len_find = len(finded)
    text = f"<b>⎈ 𝑻𝒐𝒕𝒂𝒍 𝑮𝒂𝒕𝒆𝒘𝒂𝒚𝒔 ⪢</b> <code>{len_find}</code>\n"
    for a in finded:
        text += f"""
╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾
<b>⎈ {a['gate_name']} ⪢</b> <code>/{a['cmd_name']} cc|mm|yy|cv</code>
<b>⎈ 𝑺𝒕𝒂𝒕𝒖𝒔 ⪢</b> <code>{a['status_logo']}</code>
<b>⎈ 𝑪𝒐𝒎𝒎𝒆𝒏𝒕 ⪢</b> <code>{a['comment']}</code>
"""
    nu = [
    [
        Button.inline("Previous","home"),
        # Button.inline("Next","free1"),
    ]
]
    await m.edit(text, buttons = nu)
    # await m.edit(pin)


@callback(data="p3", owner=False)
async def _(m):
    sender = await m.get_sender()
    nu = [
    [
        Button.inline("Previous","home"),
        # Button.inline("Next","free1"),
    ]
]
    x =  await mdb.find_one("main",{'_id' : m.sender_id})
    date = x['date_registered']
    role = x['role']
    pin = f"""<b>-------------- [ 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 ] --------------</b>
<b>⎈ 𝑼𝑺𝑬𝑹 𝑰𝑫 ⪢</b> <code>{m.sender_id}</code>
<b>⎈ 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬 ⪢</b> @{sender.username}
<b>⎈ 𝑹𝑬𝑮𝑰𝑺𝑻𝑬𝑹𝑬𝑫 𝑶𝑵 ⪢</b> <code>{date}</code>
<b>⎈ 𝑺𝒕𝒂𝒕𝒖𝒔 ⪢</b> <code>{role}</code>
"""
    await m.edit(pin,buttons = nu,parse_mode='html')


@callback(data="p4", owner=False)
async def _(m):
    pin = f"""<b>𝐡𝐨𝐥𝐚, 𝐞𝐬𝐭𝐞 𝐛𝐨𝐭 𝐡𝐞𝐜𝐡𝐨 𝐩𝐚𝐫𝐚 𝐜𝐡𝐞𝐪𝐮𝐞𝐚𝐫 𝐜𝐜𝐬 𝐞𝐧 𝐦𝐚𝐬𝐚 𝐨 𝐮𝐧𝐨 𝐩𝐨𝐫 𝐮𝐧𝐨.
𝐦𝐢 𝐦𝐚𝐞𝐬𝐭𝐫𝐨 𝐞𝐬 @𝐀𝐧𝐢𝐃𝐞𝐜𝟒𝐲𝐩𝐭𝟑𝐝. 𝐦𝐞𝐝𝐢𝐚𝐧𝐭𝐞 𝐞𝐥 𝐮𝐬𝐨 𝐝𝐞𝐥 𝐥𝐞𝐧𝐠𝐮𝐚𝐣𝐞 𝐝𝐞 𝐩𝐫𝐨𝐠𝐫𝐚𝐦𝐚𝐜𝐢𝐨́𝐧 𝐩𝐲𝐭𝐡𝐨𝐧. 𝐬𝐢 𝐡𝐚𝐲 𝐚𝐥𝐠𝐮́𝐧 𝐞𝐫𝐫𝐨𝐫 𝐨 𝐟𝐚𝐥𝐥𝐚, 𝐢𝐧𝐟𝐨𝐫𝐦𝐞 𝐚 𝐥𝐨𝐬 𝐚𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐝𝐨𝐫𝐞𝐬 𝐝𝐞𝐥 𝐛𝐨𝐭 𝐨 𝐦𝐞𝐝𝐢𝐚𝐧𝐭𝐞 𝐞𝐥 𝐜𝐨𝐦𝐚𝐧𝐝𝐨 /𝐫𝐞𝐩𝐨𝐫𝐭. 𝐠𝐫𝐚𝐜𝐢𝐚𝐬 𝐟𝐞𝐥𝐢𝐳 𝐱𝐜𝐡𝐞𝐜𝐤</b>
"""    
    nu = [
    [
        Button.inline("Previous","home"),
        # Button.inline("Next","free1"),
    ]
]
    await m.edit(pin,buttons = nu,parse_mode='HTML')

@callback(data="home",owner=False)
async def _(m):
    nu = [
    [
        Button.inline("𝑭𝒓𝒆𝒆 𝑮𝒂𝒕𝒆𝒔","p1"),
        Button.inline("𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑮𝒂𝒕𝒆𝒔","p2"),
    ],    [
        Button.inline("𝑴𝒚 𝒊𝒏𝒇𝒐","p3"),
        Button.inline("𝑨𝒃𝒐𝒖𝒕 𝑩𝒐𝒕","p4"),
    ],
]
    await m.edit("𝑪𝒉𝒆𝒄𝒌 𝒎𝒚 𝒑𝒍𝒖𝒈𝒊𝒏𝒔",buttons=nu),