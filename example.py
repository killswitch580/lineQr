from newqr import NewQRLogin
from linepy import LINE

newqr = NewQRLogin()
print("headers: %s" % (", ".join(newqr.HEADERS)))
header = input("header: ")
token, cert = newqr.parseLogin(newqr.loginQR(header))
client = LINE(token)