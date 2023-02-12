import re
from .tools import checkLuhn , get_bin_info

def incall_card():
    """get gate info."""
    def inner(func):
        async def wrap(*args, **kwargs ):
            m = args[0]
            if m.is_reply:
                m =await m.get_reply_message()
                text = m.text
            else:
                if 'api' in m.text:
                    text = m.text.split('|', maxsplit=1)[1]
                else:
                    text = m.text
                    
            text = text.replace('\n',' ').replace('\r',' ')
            input = re.findall(r"[0-9]+", text)
            if not input or len(input) < 3:
                await m.sod('''<code>⎈ 𝑭𝒐𝒓𝒎𝒂𝒕 ⪢ <i>cc|mm|yy|cvv</i></code>
<b>⎈ 𝑬𝒏𝒕𝒆𝒓 𝒂 𝒗𝒂𝒍𝒊𝒅 𝒄𝒂𝒓𝒅 ⎈</b>''',parse_mode="HTML" , time = 5)
                return
            if len(input) == 3:
                cc = input[0]
                if not checkLuhn(cc): return await m.sod('''<code>⎈ 𝑭𝒐𝒓𝒎𝒂𝒕 ⪢ <i>cc|mm|yy|cvv</i></code>
<b>⎈ 𝑬𝒏𝒕𝒆𝒓 𝒂 𝒗𝒂𝒍𝒊𝒅 𝒄𝒂𝒓𝒅 ⎈</b>''',parse_mode="HTML" , time = 5)
                if len(input[1]) == 3:
                    mes = input[2][:2]
                    ano = input[2][2:]
                    cvv = input[1]
                else:
                    mes = input[1][:2]
                    ano = input[1][2:]
                    cvv = input[2]
            else:
                cc = input[0]
                if len(input[1]) == 3:
                    mes = input[2]
                    ano = input[3]
                    cvv = input[1]
                else:
                    mes = input[1]
                    ano = input[2]
                    cvv = input[3]
                if  len(mes) == 2 and (mes > '12' or mes < '01'):
                    ano1 = mes
                    mes = ano
                    ano = ano1
            
            if cc[0] == 3 and len(cc) != 15 or len(cc) != 16 or int(cc[0]) not in [3,4,5,6]:
                await m.sod('''<code>⎈ 𝑭𝒐𝒓𝒎𝒂𝒕 ⪢ <i>cc|mm|yy|cvv</i></code>
<b>⎈ 𝑬𝒏𝒕𝒆𝒓 𝒂 𝒗𝒂𝒍𝒊𝒅 𝒄𝒂𝒓𝒅 ⎈</b>''',parse_mode="HTML",time = 5)
                return
            if len(mes) not in [2 , 4] or len(mes) == 2 and mes > '12' or len(mes) == 2 and mes < '01':
                await m.sod('''<code>⎈ 𝑭𝒐𝒓𝒎𝒂𝒕 ⪢ <i>cc|mm|yy|cvv</i></code>
<b>⎈ 𝑬𝒏𝒕𝒆𝒓 𝒂 𝒗𝒂𝒍𝒊𝒅 𝒎𝒐𝒏𝒕𝒉 ⎈</b>''',parse_mode="HTML", time = 5)
                return
            if len(ano) not in [2,4] or len(ano) == 2 and ano < '21' or len(ano)  == 4 and ano < '2021' or len(ano) == 2 and ano > '29' or len(ano)  == 4 and ano > '2029':
                await m.sod('''<code>⎈ 𝑭𝒐𝒓𝒎𝒂𝒕 ⪢ <i>cc|mm|yy|cvv</i></code>
<b>⎈ 𝑬𝒏𝒕𝒆𝒓 𝒂 𝒗𝒂𝒍𝒊𝒅 𝒚𝒆𝒂𝒓 ⎈</b>''',parse_mode="HTML",time = 5)
                return
            if cc[0] == 3 and len(cvv) != 4 or len(cvv) != 3:
                await m.sod('''<code>⎈ 𝑭𝒐𝒓𝒎𝒂𝒕 ⪢ <i>cc|mm|yy|cvv</i></code>
<b>⎈ 𝑬𝒏𝒕𝒆𝒓 𝒂 𝒗𝒂𝒍𝒊𝒅 𝒄𝒗𝒗 ⎈</b>''',parse_mode="HTML" ,time = 5)
                return 
            bin =  get_bin_info(cc[:6])
            if not bin:
                await m.reply("Change your bin i will not check with this bin.")
                return
            if (cc,mes,ano ,cvv):
                if len(ano) == 2:
                    ano = "20"+ str(ano)
                await func(*args,(cc, mes, ano, cvv , bin) ,**kwargs)
        return wrap
    return inner
