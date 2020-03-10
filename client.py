import requests

HEADERS = ["android_lite", "android", "ios_ipad", "ios", "chrome", "desktopwin", "desktopmac"]
BASE_HOST = "https://usqf.cf/"
print("Headers: %s" % (", ".join(headers for headers in HEADERS)))
HEADER = input("Header: ").strip()

if HEADER not in HEADERS:
    print("Invalid HEADER")
    exit()

def loginQR(headers, callback=lambda x: print(x)):
    result = requests.get(BASE_HOST + "login?headers=" + headers).json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    callback("Login Url: %s" % (result["url"]))
    result = requests.get(BASE_HOST + result["callback"]).json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    callback("Pin Code: %s" % (result["pincode"]))
    result = requests.get(BASE_HOST + result["callback"]).json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    return result

def loginQRWithWebPinCode(headers, callback=lambda x: print(x)):
    result = requests.get(BASE_HOST + "login?headers=" + headers).json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    callback(
        "Pin Url: %sawaitPinCode?session=%s&lang=th" % (BASE_HOST, result["session"]) + "\n"
        "Login Url: %s" % (result["url"])
    )
    result = requests.get(BASE_HOST + result["callback"]).json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    result = requests.get(BASE_HOST + result["callback"]).json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    return result

def loginQRWithCert(headers, certificate, callback=lambda x: print(x)):
    result = requests.get(BASE_HOST + "login?headers=" + headers + "&certificate=" + certificate).json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    callback("Login Url: %s" % (result["url"]))
    result = requests.get(BASE_HOST + result["callback"]).json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    return result

def loginQRWithCertV2(headers, certificate, callback=lambda x: print(x)):
    result = requests.get(BASE_HOST + "login?headers=" + headers + "&certificate=" + certificate + "&type=2").json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    callback("Login Url: %s" % (result["url"]))
    result = requests.get(BASE_HOST + result["callback"]).json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    if result["status"] != 409:
        return result
    result = requests.get(BASE_HOST + result["callback"]).json()
    if result["status"] != 200:
        raise Exception(result["reason"])
    return result

print(loginQRWithWebPinCode(HEADER))
