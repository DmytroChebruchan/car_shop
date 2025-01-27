import base64
import hashlib

import ecdsa
import requests
from django.conf import settings

from carshop.models import Order

PUBLIC_KEY = "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUZrd0V3WUhLb1pJemowQ0FRWUlLb1pJemowREFRY0RRZ0FFc05mWXpNR1hIM2VXVHkzWnFuVzVrM3luVG5CYgpnc3pXWnhkOStObEtveDUzbUZEVTJONmU0RlBaWmsvQmhqamgwdTljZjVFL3JQaU1EQnJpajJFR1h3PT0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg=="
REDIRECT_URL = (
    "https://boiling-fortress-51276-88bb58822abe.herokuapp.com/payment_status/"
)


def verify_signature(request):
    x_sing_base64 = request.headers["X-Sign"]
    body_test = request.body
    print(body_test)
    public_key_bytes = base64.b64decode(PUBLIC_KEY)
    signature_bytes = base64.b64decode(x_sing_base64)
    pub_key = ecdsa.VerifyingKey.from_pem(public_key_bytes.decode())

    ok = pub_key.verify(
        signature_bytes,
        body_test,
        sigdecode=ecdsa.util.sigdecode_der,
        hashfunc=hashlib.sha256,
    )
    print(ok)
    if not ok:
        raise Exception("Signature is not valid")


def create_invoice(order: Order, cars, webhook_url):
    amount = 0
    basket_order = []
    for car in cars:
        sum_ = car.car_type.price * 100
        amount += sum_
        basket_order.append(
            {
                "name": f"{car.car_type.brand} {car.car_type.name}",
                "qty": 1,
                "sum": sum_,
                "icon": car.car_type.image.url,
                "unit": "шт.",
            }
        )
    merchants_info = {
        "reference": str(order.id),
        "destination": "Купівля машин",
        "basketOrder": basket_order,
    }
    request_body = {
        "redirectUrl": REDIRECT_URL,
        "webHookUrl": webhook_url,
        "amount": amount,
        "merchantPaymInfo": merchants_info,
    }
    headers = {"X-Token": settings.MONOBANK_TOKEN}
    r = requests.post(
        "https://api.monobank.ua/api/merchant/invoice/create",
        json=request_body,
        headers=headers,
    )
    r.raise_for_status()
    order.invoice_id = r.json()["invoiceId"]
    order.invoice_url = r.json()["pageUrl"]
    order.status = "created"
    order.save()
