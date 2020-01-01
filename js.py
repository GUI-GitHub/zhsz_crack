import execjs

data = ""

with open("js/DES3.js") as f:
    data = f.read()

ctx = execjs.compile(data)

def encrypt(input):
    ctx.call("encrypt",input)

def decrypt(input):
    ctx.call("decrypt",input)
