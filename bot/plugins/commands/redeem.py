from time import gmtime, strftime
import time
from veriable.veriable import LOG_CHAT
from .decoretors import msg_send
from ...utils.user_info import user_info
from bot import mdb


@msg_send(cmd="redeem")
async def _(m):
    params = m.pattern_match.group(1).strip()
    first = await m.reply('đ©đźđčđ¶đ±đźđđ¶đ»đŽ đœđżđŒđđ¶đ±đČđ± đ¶đ»đœđđ')
    if not params or not ( params.startswith('KEY-') and params.endswith('-PREMIUM') ):
        await first.edit('''<b>â đ­đđđđđ âȘą </b><code>/redeem key</code>
<b>â đŹđđđđ đđ đđđđđ đđđđđđ â</b>''',parse_mode="HTML")
        return
    is_key = await mdb.find_one('keys', {'_id': params})
    if not is_key:
        await first.edit("đ·đđđđđđđ đđđ đđđ đđđđđđđđđ đđđđđđđ <code>@AniDec4ypt3d</code>.",parse_mode='HTML',  time = 5)
        return
    user = await user_info(m)
    if user['type'] == 'P' and params.startswith('KEY-') and params.endswith('-PREMIUM'):
        await first.edit("đșđđđđ đđđ đđđ đđđđđđđ đ đđđđđđđ đđđđ, đđđ đđđđđ đđđđđđđ đđđ đđđđđ.",parse_mode='HTML')
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
        await first.edit(f'''âŸâŸâŸâŸâŸâŸâŸâŸâŸ [ đČđđ đčđđđđđđđ ] âŸâŸâŸâŸâŸâŸâŸâŸâŸ
<b>â đ·đđđđđ âȘą</b> <code>{is_key['data']} {is_key['time_type']}s</code>
<b>â đ·đđđ âȘą</b> <code>Premium Plan</code>''',parse_mode='HTML')
        await m.client.send_message(LOG_CHAT,  f"{m.sender_id} Claimed Key: {params}")
        if m.is_private != True:
            await m.client.send_message(m.sender_id,  f'''đđđđ đđđđđđđđđđ đđđ đđđđ đđđđđđđ!
âŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸâŸ
<b>â đ·đđđ âȘą</b> <code>Premium Plan</code>
''')
    else:
        await m.sod("**đŹđđđđđđđđđŹđđđđđ­đđđđ 402**")