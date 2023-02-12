import inspect
import os, sys
import string
from asyncio import sleep
import random
import time 

from telethon.tl.types import MessageService
from telethon.tl.types import Message, MessageEntityTextUrl
from telethon.errors.rpcerrorlist import MessageDeleteForbiddenError

from ...core import client
from bot import  mdb
import aiohttp
from telethon import utils
from telethon.tl.custom.sendergetter import SenderGetter

async def web_search(
    link:str = None,
    data: str = None,
    json: dict = None,
    params: dict = None,
    headers: dict = None,
    post:bool =  False,
    r_json: bool = False,
    r_content: bool = False,
    r_real: bool = False,
    **kwargs
):
    """
    Search for a link on web
    """
    if not headers:
        headers = {}

    if json:
        headers.update({"Content-Type": "application/json"})
    if data:
        headers.update({"Content-Type": "application/x-www-form-urlencoded"})
    async with aiohttp.ClientSession(headers = headers) as session:
        if post or data or json:
            async with session.post(link, data=data, json=json,**kwargs) as resp:
                if r_json:
                    return await resp.json()
                if r_content:
                    return await resp.read()
                if r_real:
                    return resp
                return await resp.text()
        else:
            async with session.get(link, params=params, **kwargs) as resp:
                if r_json:
                    return await resp.json()
                if r_content:
                    return await resp.read()
                if r_real:
                    return resp
                return await resp.text()


async def send_main(m, text = None,**kwargs):
    time = kwargs.get("time", None)
    edit_time = kwargs.get("edit_time", None)
    if time:
        del kwargs['time']
    if edit_time:
        del kwargs['edit_time']
    if "link_preview" not in kwargs:
        kwargs.update({"link_preview": False})
    if m.out and not isinstance(m, MessageService):
        if edit_time:
            await sleep(edit_time)
        ok = await m.edit(text, **kwargs)
    else:
        kwargs["reply_to"] = m.reply_to_msg_id or m
        ok = await client.send_message(m.chat_id, text, **kwargs)
    if time:
        await sleep(time)
        await m.try_delete()
        return await ok.delete()
    return ok



async def send(m: object, text: str = None, **kwargs):
    kwargs["time"] = kwargs.get("time", 7)
    return await send_main(m, text, **kwargs)





async def try_delete(m: Message):
    try:
        await m.delete()
    except MessageDeleteForbiddenError:
        pass


def random_string(length=3):
    """Generate random string of 'n' Length"""
    return "".join(random.choices(string.ascii_uppercase, k=length))
    # return "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))

def random_integer(length=5):
    """Generate random string of 'n' Length"""
    return "".join(random.choices(string.digits, k=length))



async def haste_bin(m: Message, text:None, **kwargs):
    if text:
        doc = await web_search('https://www.toptal.com/developers/hastebin/documents', json = str(text),r_json= True, **kwargs)
        if 'key' in doc:
            raw_key = doc['key']
        return 'https://www.toptal.com/developers/hastebin/raw/'+ raw_key
    else:
        if hasattr(m, "text"):
            doc = await web_search('https://www.toptal.com/developers/hastebin/documents', json = str(m.text),r_json= True, **kwargs)
            if 'key' in doc:
                raw_key = doc['key']
            return 'https://www.toptal.com/developers/hastebin/raw/'+ raw_key
        else:
            return 'https://www.toptal.com/developers/hastebin/raw/enoyegiyer'

def save_lives(m, cards: str):
    with open('lives/lives.txt', 'a') as f:
        return f.write(str(cards) + '\n')


def get_full_user_info(m: Message):
    return m.sender.username

def full_name(m: Message):
    return utils.get_display_name(m.sender)


setattr(random, "random_string", random_string)
setattr(random, "random_integer", random_integer)
setattr(Message, "sod", send_main)
setattr(Message, "try_delete", try_delete)
setattr(Message, "haste_bin", haste_bin)

setattr(Message, "mdb", mdb)
setattr(Message, "utils", utils)
setattr(Message, "username", get_full_user_info)
setattr(Message, "full_name", full_name)

setattr(Message, "save_lives", save_lives)