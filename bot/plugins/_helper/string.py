import os, sys, inspect
from pathlib import Path
import yaml , glob
import logging
from ...core import adb
import pathlib
from ...core.logger import log
all_langs = glob.glob('configs/*.yml')

LANGS = {}

for lang in all_langs:
    stem = Path(lang).stem
    with open(os.path.join(os.getcwd(), Path(lang)), 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.CLoader)
        
    log.debug("Importing {} Keys From {} language".format(len(data) , stem))
    if stem not in LANGS:
        LANGS[stem] = data 
        # print(LANGS[stem])
    else:
        LANGS[stem].update(data)
        # print(LANGS[stem])

async def get_lang(user_id: int):
    """Get User Language"""
    lang = await adb.get("LANGUAGE_" + str(user_id))
    if lang:
        return lang
    return "en"


def get_strings(cmd_name: str = None):
    """Get all strings for a command"""
    def strings(func):
        async def wrap(*args, **kwargs):
            m = args[0]
            user_id = m.sender_id
            user_lang = await get_lang(user_id)
            if user_lang in LANGS:
                lang = LANGS[user_lang]
                if cmd_name in lang:
                    mod =  lang[cmd_name]
                else:
                    await m.sod("{} Language Not Found.".format(cmd_name), time = 5)
                    return
            else:
                await m.sod("{} Language is not supported now..".format(user_lang.title()), time = 5)
                return
            if mod:
                await func(*args,mod, **kwargs)
        return wrap
    return strings