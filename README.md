# lineQr [![Status](https://img.shields.io/website?down_color=red&down_message=Currently%20Down&up_color=green&up_message=Still%20Working&url=https%3A%2F%2Fusqf.cf%2F)]()
Generate Line's Cert/AuthToken by QRCode 

Example
------------
```python
from newqr import NewQRLogin
from linepy import LINE

newqr = NewQRLogin()
print("headers: %s" % (", ".join(newqr.HEADERS)))
header = input("header: ")
token, cert = newqr.parseLogin(newqr.loginQR(header))
client = LINE(token)
```
[LINEPY](https://github.com/crash-override404/linepy-modified) required
