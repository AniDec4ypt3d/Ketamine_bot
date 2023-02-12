from time import gmtime, strftime
import time
from veriable.veriable import LOG_CHAT
from .decoretors import msg_send
from ...utils.user_info import user_info
from bot import mdb


@msg_send(cmd="redeem")
async def _(m):
    params = m.pattern_match.group(1).strip()
    first = await m.reply('𝗩𝗮𝗹𝗶𝗱𝗮𝘁𝗶𝗻𝗴 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗶𝗻𝗽𝘂𝘁')
    if not params or not ( params.startswith('KEY-') and params.endswith('-PREMIUM') ):
        await first.edit('''<b>⎈ 𝑭𝒐𝒓𝒎𝒂𝒕 ⪢ </b><code>/redeem key</code>
<b>⎈ 𝑬𝒏𝒕𝒆𝒓 𝒊𝒏 𝒗𝒂𝒍𝒊𝒅 𝒇𝒐𝒓𝒎𝒂𝒕 ⎈</b>''',parse_mode="HTML")
        return
    is_key = await mdb.find_one('keys', {'_id': params})
    if not is_key:
        await first.edit("𝑷𝒓𝒐𝒗𝒊𝒅𝒆𝒅 𝒌𝒆𝒚 𝒏𝒐𝒕 𝒂𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆 𝒄𝒐𝒏𝒕𝒂𝒄𝒕 <code>@AniDec4ypt3d</code>.",parse_mode='HTML',  time = 5)
        return
    user = await user_info(m)
    if user['type'] == 'P' and params.startswith('KEY-') and params.endswith('-PREMIUM'):
        await first.edit("𝑺𝒐𝒓𝒓𝒚 𝒚𝒐𝒖 𝒂𝒓𝒆 𝒂𝒍𝒓𝒆𝒂𝒅𝒚 𝒂 𝒑𝒓𝒆𝒎𝒊𝒖𝒎 𝒖𝒔𝒆𝒓, 𝒍𝒆𝒕 𝒆𝒙𝒊𝒔𝒕 𝒑𝒓𝒆𝒎𝒊𝒖𝒎 𝒆𝒏𝒅 𝒇𝒊𝒓𝒔𝒕.",parse_mode='HTML')
        return
    exp = is_key['data'] * 3600 if is_key['time_type'] == 'hour' else is_key['data'] * 86400
    filter = {'_id': m.sender_id}
    data = {
        '$addToSet': {
            'keys': params,
            'claimed_date': strftime("%Y-%m-%d", gmtime()),
        },
        '$set': {
            'type': 'P',
            'role': 'Premium User',
            'expire_days': int(time.time()) + exp,
        }
    }
    
    insert = await mdb.update_one('main', filter,data)
    if insert:
        insert = await mdb.delete('keys', {'_id': params})
        await first.edit(f'''╾╾╾╾╾╾╾╾╾ [ 𝑲𝒆𝒚 𝑹𝒆𝒅𝒆𝒆𝒎𝒆𝒅 ] ╾╾╾╾╾╾╾╾╾
<b>⎈ 𝑷𝒆𝒓𝒊𝒐𝒅 ⪢</b> <code>{is_key['data']} {is_key['time_type']}s</code>
<b>⎈ 𝑷𝒍𝒂𝒏 ⪢</b> <code>Premium Plan</code>''',parse_mode='HTML')
        await m.client.send_message(LOG_CHAT,  f"{m.sender_id} Claimed Key: {params}")
        if m.is_private != True:
            await m.client.send_message(m.sender_id,  f'''𝒀𝒐𝒖𝒓 𝒎𝒆𝒎𝒃𝒆𝒓𝒔𝒉𝒊𝒑 𝒉𝒂𝒔 𝒃𝒆𝒆𝒏 𝒖𝒑𝒅𝒂𝒕𝒆𝒅!
╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾
<b>⎈ 𝑷𝒍𝒂𝒏 ⪢</b> <code>Premium Plan</code>
''')
    else:
        await m.sod("**𝑬𝒙𝒄𝒆𝒑𝒕𝒊𝒐𝒏𝑬𝒓𝒓𝒐𝒓𝑭𝒐𝒖𝒏𝒅 402**")