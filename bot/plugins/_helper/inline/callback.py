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
    text = f"<b>â đ»đđđđ đźđđđđđđđ âȘą</b> <code>{len_find}</code>\n"
    for a in finded:
        text += f"""
âŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸ
<b>â {a['gate_name']} âȘą</b> <code>/{a['cmd_name']} cc|mm|yy|cv</code>
<b>â đșđđđđđ âȘą</b> <code>{a['status_logo']}</code>
<b>â đȘđđđđđđ âȘą</b> <code>{a['comment']}</code>
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
    text = f"<b>â đ»đđđđ đźđđđđđđđ âȘą</b> <code>{len_find}</code>\n"
    for a in finded:
        text += f"""
âŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸ
<b>â {a['gate_name']} âȘą</b> <code>/{a['cmd_name']} cc|mm|yy|cv</code>
<b>â đșđđđđđ âȘą</b> <code>{a['status_logo']}</code>
<b>â đȘđđđđđđ âȘą</b> <code>{a['comment']}</code>
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
    pin = f"""<b>-------------- [ đđ§đđšđ«đŠđđ­đąđšđ§ ] --------------</b>
<b>â đŒđșđŹđč đ°đ« âȘą</b> <code>{m.sender_id}</code>
<b>â đŒđșđŹđčđ”đšđŽđŹ âȘą</b> @{sender.username}
<b>â đčđŹđźđ°đșđ»đŹđčđŹđ« đ¶đ” âȘą</b> <code>{date}</code>
<b>â đșđđđđđ âȘą</b> <code>{role}</code>
"""
    await m.edit(pin,buttons = nu,parse_mode='html')


@callback(data="p4", owner=False)
async def _(m):
    pin = f"""<b>đĄđšđ„đ, đđŹđ­đ đđšđ­ đĄđđđĄđš đ©đđ«đ đđĄđđȘđźđđđ« đđđŹ đđ§ đŠđđŹđ đš đźđ§đš đ©đšđ« đźđ§đš.
đŠđą đŠđđđŹđ­đ«đš đđŹ @đđ§đąđđđđđČđ©đ­đđ. đŠđđđąđđ§đ­đ đđ„ đźđŹđš đđđ„ đ„đđ§đ đźđđŁđ đđ đ©đ«đšđ đ«đđŠđđđąđšÌđ§ đ©đČđ­đĄđšđ§. đŹđą đĄđđČ đđ„đ đźÌđ§ đđ«đ«đšđ« đš đđđ„đ„đ, đąđ§đđšđ«đŠđ đ đ„đšđŹ đđđŠđąđ§đąđŹđ­đ«đđđšđ«đđŹ đđđ„ đđšđ­ đš đŠđđđąđđ§đ­đ đđ„ đđšđŠđđ§đđš /đ«đđ©đšđ«đ­. đ đ«đđđąđđŹ đđđ„đąđł đ±đđĄđđđ€</b>
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
        Button.inline("đ­đđđ đźđđđđ","p1"),
        Button.inline("đ·đđđđđđ đźđđđđ","p2"),
    ],    [
        Button.inline("đŽđ đđđđ","p3"),
        Button.inline("đšđđđđ đ©đđ","p4"),
    ],
]
    await m.edit("đȘđđđđ đđ đđđđđđđ",buttons=nu),