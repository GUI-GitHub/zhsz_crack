from js import *
from urllib.request import *
from urllib.error import *
from urllib.parse import *
import base64



def get(user,pwd):
    r = Request("http://zhsz.bjedu.cn/web/login/validate",method="POST")
    
    user = base64.b64encode(encrypt(user))
    pwd = base64.b64encode(encrypt(pwd))
    sign = base64.b64encode(user)

    data = {
        "user":user,
        "pwd":pwd,
        "save":0,
        "sign":sign
    } 
    data = urlencode(data)
    r.data = data
    r = urlopen(r)
    return r


if __name__ == "__main__":
    print(get("1","1").read())