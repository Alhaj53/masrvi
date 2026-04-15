import requests
import json
import uuid
import sys

# -----------------------
# استقبال المدخلات من Flask
# -----------------------

otp = sys.argv[1]
access_token = sys.argv[2]
num = sys.argv[3]
current_password = sys.argv[4]

# -----------------------
# إعداد session
# -----------------------

install_id = str(uuid.uuid4())
session = requests.Session()

BASE_URL = "https://22201.tagpay.fr/api/client/v1"

COMMON_HEADERS = {
    "User-Agent": "Masrvi / 25.09.6713(6713)",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json"
}

# -----------------------
# طلب OTP
# -----------------------

url3 = "https://22201.tagpay.fr/api/client/v1/oauth2/otp"

payload3 = {
    "grant_type": "password",
    "client_id": "#####",
    "client_secret": "#####",
    "scope": [],
    "username": access_token,
    "password": otp,
    "install_id": install_id
}

headers3 = {
    "User-Agent": "Masrvi2 / 25.09.6713(6713)",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json"
}

response3 = requests.post(
    url3,
    json=payload3,
    headers=headers3
)

otp_data = response3.json()
otp_token = otp_data.get("access_token")

if not otp_token:
    print(json.dumps({
        "status": "fail",
        "message": "OTP failed"
    }))
    sys.exit()

# -----------------------
# database يجب أن يكون موجود
# -----------------------

database = {
    0: "iVBORw0KGgoAAAANSUhEUgAAAHwAAAB8AQMAAACR0Eb9AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAL9JREFUSInt0zEOhCAQBVAMBSVH4CgeTY7mUTiCpYVhHGLhfD7JZrfYikksfCYDyB/nZs36XHLhexDJAEmkAGwiJ7YQbLIoiAXfwHYNDXYDUUoCSJIDrLtW7XtY0DUBtvN5XtCvq4XWMF0dRADdQ6z2KAoBII/AHNc38ADuJ1gY8gu1g/AXoGV5Y8Otf3v8jEA/eXANOwJd5eCySxcHCgxFikJHsdTgegguRZvCT+NBA0QjxkNIY0qDTKM+a9awbrjnrg9cY3dfAAAAAElFTkSuQmCC",
    1: "iVBORw0KGgoAAAANSUhEUgAAAHwAAAB8AQMAAACR0Eb9AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAADFJREFUSIljYBgFo4AMwPwHTYAfXcAeTYDxP5oAO7qAPH0EMFw6KjAqMCowCkYBSQAAjXhFBPlDmZUAAAAASUVORK5CYII=",
    2: "iVBORw0KGgoAAAANSUhEUgAAAHwAAAB8AQMAAACR0Eb9AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAKVJREFUSInt07ENwyAQBVAQBeWNwCiMRkbzKB7BpQuLb9zlfyzhRJHS8DuerOPOgHMzM+OUg9cBYDBgIcjAxiWAnQAAVfV3UHnXNYPhZQQRl71DFbDa6hIcQ2h903RfwBUqegf+cwhyDj3EOgKTw3Wpg10gK5RNACuvvULQ/xN1NtNRknaetdGifckl/EkbWdvQ1+Hkpve7Rt21vR/QR+k/MDPzMCdgeYvq3JSF0QAAAABJRU5ErkJggg==",
    3: "iVBORw0KGgoAAAANSUhEUgAAAHwAAAB8AQMAAACR0Eb9AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAL9JREFUSInt07sRxCAMBFAYAoeUQCmUZpfmUijBoQOGPV3mXXmOuZwdJ36B+AiFsLIyD27+3wCGApwEFWgEO3BxTXDVaNCfkAwGr9qqwJHB8P0eycPKEHQPkeE2OB5QXiFw5pAUNoU8BIrC3vkf2hi95KBtMDgUzmkNt4rsY4Pbuj+trJsUom4kzGH/CbUZtP/g0hqXLOvhFihdzlKGnDZD7iPb05aXDJ4xNw1J5yXqRPmZq9rsrIMctbUrK6/5AKkKkzmgRRuGAAAAAElFTkSuQmCC",
    4: "iVBORw0KGgoAAAANSUhEUgAAAHwAAAB8AQMAAACR0Eb9AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAHxJREFUSIntziEOgDAQRNFtKip7hB6lRyuOa+G4Bg6Lo4J0CXIHMQRDSPrlU1+k13tTagCZQkFQBg7BIwQKESFRyDtAWRnobMHpaMHfIVgIDSAeDFIFyBuDsgDoRMDpYMGrWAg3aADxAEiVQd4AysJAr9r3IAJjv4Je70kniyyNqv5M5p4AAAAASUVORK5CYII=",
    5: "iVBORw0KGgoAAAANSUhEUgAAAHwAAAB8AQMAAACR0Eb9AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAKhJREFUSInt0rENwzAMBEAaLlR6BI3i0azRMopHcGkggj5U538FEZzClb68Rk+KZiMj9wPPT5gegblIr38g34bQh7OBWASAF8Eb2K+w+LCnQlYoCujAHpEIUqAiEb5nAn+TwVtR1QobwWG20jCe9ehBfATo2dqSQatX4OGaaZt9ZFnhUmxmqFtPFwj6L6G5df3sSc/B9GBsA3j6KEdXn0kEBr3lkZFv+QBqsJl9nTuIVgAAAABJRU5ErkJggg==",
    6: "iVBORw0KGgoAAAANSUhEUgAAAHwAAAB8AQMAAACR0Eb9AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAN1JREFUSIntk7ENAyEMRYmuoLwRPAqjcRtkhIwSpBRZgxEorzjdj93xTaRTpJT8jidkf39wCFNT18oHnxeAwQoUAgJUAgnYuSbAVeHATcHJXZtQ34gtOqCXtt7XqWUIaAuyKvsXkHuQ2iWogTWAPIByDYSmV5egUQJeLmS8gUbg7jLFw2WKJ/gtgQHURH1hqfduteLCwELundnTM2guEwOUml1P7SeQ/wDMA/lI3ukAxA8nh3660oHVB7RahFsHIqoQWPwzDNsw7IttFK9Yct/BtrIQiH6Rg6s5NfVdHzZ0tl+g5INtAAAAAElFTkSuQmCC",
    7: "iVBORw0KGgoAAAANSUhEUgAAAHwAAAB8AQMAAACR0Eb9AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAHFJREFUSInt0LENgDAQQ9EgipSMwCgZjYzGKIxASYFISBkbyQQhaM7dPema75zN1ryQzs3/Q1mK9d0xwEdPcAB4gh1g0LABjAQrQCBYACYJ3Icg1veTYAgcDEEH4z4SOBjCC8Eu+ij4KFh7QR3MZru3DKTMY/3cTbi/AAAAAElFTkSuQmCC",
    8: "iVBORw0KGgoAAAANSUhEUgAAAHwAAAB8AQMAAACR0Eb9AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMFJREFUSIntk7ERAyEMBPE4+JASKOVL40ujFEog/ID5s8h0kmYc2CHK2EA6aYeUdu36Wi9MBgdwEShAJ1CBQQDAzT2BR4O3BTIEYNALzc0QRuCRNgSmDGo6qGzC4A5A/RFk29SDFUwnPR4LILuo99os04FEC19sHZlNOQ1O1GlBJIqaBqImi8q4Ai9Nx4g0VB3kHAE4CfQIjH+DEQAO5qIv2RqUJZsAzD0yWjH2AQ/U22sI7ZNKb9995GS/+q5dYX0AQwSzElqMhjkAAAAASUVORK5CYII=",
    9: "iVBORw0KGgoAAAANSUhEUgAAAHwAAAB8AQMAAACR0Eb9AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAN1JREFUSInt07kRAyEMBdD1OCCkBJVCabgTt0InpgTCDZiVvzK+8CwuAGW8PQAdx7FjxzIe2hiiXgxJ9UWQVSv/QvknT8A5QgB0D7RN1JIJRGEEHV+NB0kndiZogDIeFMecIE8wXsaeriG1FeR7qP8AJTXb5cak4vpPBkvQCHIhhQRIMkFUV7rgwUr5GcGK/aZqA4Qga2cQbeIapCTXdscMdQX5Fux1KrYBtYNtSSDNtZRYkh0EasvYXZ9iJdTJAVmfmp9gmpdpoizJlQBDWAgwprTGQTrDNOo7dvyMLzbxsSA7uYS5AAAAAElFTkSuQmCC",
}

reverse_db = {v: k for k, v in database.items()}

# -----------------------
# keyboard
# -----------------------

def get_keyboard(token):

    headers = COMMON_HEADERS.copy()
    headers["authorization"] = f"Bearer {token}"

    res = session.get(
        f"{BASE_URL}/keyboard",
        params={
            "font": "DMSans-Medium",
            "width": "124",
            "fontSize": "62"
        },
        headers=headers
    )

    data = res.json()

    return data.get("images", []), data.get("id")


def extract(images):

    result = {}

    for i, img in enumerate(images):

        num_value = reverse_db.get(img)

        if num_value is not None:

            result[num_value] = i

    return result


def build(pin, mapping):

    digits = [int(x) for x in pin]

    values = [mapping.get(d) for d in digits]

    if None in values:
        return None

    return values


# -----------------------
# current pin
# -----------------------

images1, id_old = get_keyboard(otp_token)

map1 = extract(images1)

current_pin = build(current_password, map1)

if not current_pin:

    print(json.dumps({
        "status": "fail",
        "message": "current PIN failed"
    }))

    sys.exit()

# -----------------------
# new pin
# -----------------------

images2, id_new = get_keyboard(otp_token)

map2 = extract(images2)

new_pin = build("6024", map2)

if not new_pin:

    print(json.dumps({
        "status": "fail",
        "message": "new PIN failed"
    }))

    sys.exit()

# -----------------------
# تغيير كلمة السر
# -----------------------

payload = {
    "currentPincode": {
        "id": id_old,
        "value": current_pin
    },
    "newPincode": {
        "id": id_new,
        "value": new_pin
    }
}

headers_put = {
    "User-Agent": "Masrvi / 25.09.6713(6713)",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "authorization": f"Bearer {otp_token}"
}

res = session.put(
    f"{BASE_URL}/client/pincode",
    json=payload,
    headers=headers_put
)

print(json.dumps({
    "status": "success",
    "response": res.text
}))
