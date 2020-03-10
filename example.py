from newqr import NewQRLogin
from linepy import LINE

# HEADER must be same as config.py

newqr = NewQRLogin()

print("headers: %s" % (", ".join(newqr.HEADERS)))
header = input("header: ")

method = newqr.loginQRWithWebPinCode
token, cert = newqr.parseLogin(method(header))

client = LINE(token)
