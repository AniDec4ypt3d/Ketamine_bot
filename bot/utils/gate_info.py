import time
from bot import mdb 
from veriable.veriable import LOG_CHAT , ADMINS

from requests.exceptions import ProxyError
from ..core import adb
from ..utils import user_info



def get_gate_info(cmd_name: str = None):
    """get gate info."""
    def strings(func):
        async def wrap(*args, **kwargs):
            m = args[0]
            user = await user_info(m)
            if not user:
                return await m.reply("Error While Getting User Info")
                
            
            if user['type'] == "P":
                if user['expire_days'] < time.time():
                    filter = {'_id': m.sender_id}
                    await m.reply("𝒀𝒐𝒖𝒓 𝒎𝒆𝒎𝒃𝒆𝒓𝒔𝒉𝒊𝒑 𝒉𝒂𝒔 𝒆𝒙𝒑𝒊𝒓𝒆𝒅, 𝒄𝒐𝒏𝒕𝒂𝒄𝒕 @AniDec4ypt3d 𝒕𝒐 𝒓𝒆𝒂𝒄𝒕𝒊𝒗𝒂𝒕𝒆")
                    data = {'$set': {'type': 'F','role': 'Free User',}
    }
    
                    await mdb.update_one('main', filter,data)
                    return
                # elif user['expire_days'] - time.time() < 3600:
                #     await m.reply("Your Premium Plan will expire in 1 hour. Please contact @r0ld3x for renewing your plan.")
                #     return
            # else:
                # if m.is_private:
                #     await m.reply("you dont have to use this command in private chat. talk with @r0ld3x for access.")
                #     return
                # all_chats = await adb.get_key(f'approved_{str(m.chat_id)}')
                # if not m.is_private and not all_chats and m.sender_id in ADMINS:
                #     await m.reply("<b>𝗖𝗵𝗮𝘁 𝗶𝘀 𝘂𝗻𝗮𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱. 𝗸𝗶𝗻𝗱𝗹𝘆 𝗰𝗼𝗻𝘁𝗮𝗰𝘁 @𝗔𝗻𝗶𝗗𝗲𝗰𝟰𝘆𝗽𝘁𝟯𝗱 𝗳𝗼𝗿 𝗮𝗰𝗰𝗲𝘀𝘀 𝘁𝗼 𝘂𝘀𝗲 𝗺𝗲</b>")
                #     return
            # if is_shopify:
            #     if 'shopify_apis' in user:
            #         if len(user['shopify_apis']) < 1:
            #             return await m.reply("You have 0 Shopify APIs. Please contact @r0ld3x for more info.")
            #         api_name = m.pattern_match.group(1).split('|',maxsplit=1)[0].strip()
            #         if not api_name.startswith('api') or not api_name in user['shopify_apis'].keys():
            #             return await m.reply("Please use valid api names.")
            #         site = user['shopify_apis'].get(api_name, None)
            #         if not site:
            #             return await m.reply("Please use valid api names.")
            #         await func(*args,{'api_name':api_name,'api_site':site},user,**kwargs)
            if cmd_name:
                all_chats = await adb.get_key(f'approved_{str(m.chat_id)}')
                if not m.is_private and not all_chats and m.sender_id not in ADMINS:
                    await m.reply("<b>𝗖𝗵𝗮𝘁 𝗶𝘀 𝘂𝗻𝗮𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱. 𝗸𝗶𝗻𝗱𝗹𝘆 𝗰𝗼𝗻𝘁𝗮𝗰𝘁 @𝗔𝗻𝗶𝗗𝗲𝗰𝟰𝘆𝗽𝘁𝟯𝗱 𝗳𝗼𝗿 𝗮𝗰𝗰𝗲𝘀𝘀 𝘁𝗼 𝘂𝘀𝗲 𝗺𝗲</b>")
                    return
                gate_info = await mdb.find_one('gate', str(cmd_name))
                if gate_info['status'] == False:
                    return await m.reply(f'''<b>{gate_info['gate_name']} 𝒊𝒔 𝒖𝒏𝒅𝒆𝒓 𝑶𝑭𝑭
⎈ 𝑹𝒆𝒂𝒔𝒐𝒏 ⪢ </b><code>{gate_info['comment']}</code>''',parse_mode='HTML')
                if not gate_info:
                    await m.reply("{} gate not found.".format(cmd_name))
                    return
                # if user['antispam']:
                #     antispam =  await adb.get_key(f'antispam_{str(m.sender_id)}')
                #     if antispam:
                #         sec = time.time() - antispam
                #         if sec < user['antispam_time']:
                #             await m.reply("You can use this command in {} seconds.".format(str(user['antispam_time'] -  sec)))
                #             return
            
                if gate_info['is_paid'] and user['type'] == "F":
                    return await m.reply('''<b>𝑼𝒏𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒕𝒐 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 𝒈𝒂𝒕𝒆
⎈ 𝑹𝒆𝒂𝒔𝒐𝒏 ⪢</b> <code>𝒀𝒐𝒖 𝒂𝒓𝒆 𝒂 𝑭𝑹𝑬𝑬 𝒖𝒔𝒆𝒓</code>''',parse_mode='HTML')
                try:
                    await func(*args,gate_info,user,**kwargs)
                except ProxyError:
                    await m.reply("Proxy Error kindly mention. reported to master.")
                    await m.client.send_message(LOG_CHAT, f"{gate_info['gate_name']} s Proxy Dead")
        return wrap
    return strings