import base64
from cryptography.fernet import Fernet

def generateKey():
    key=Fernet.generate_key()
    return key.hex()
def enc(data:str,key_hex):
    """data must be b64 string"""
    f=Fernet(bytes.fromhex(key_hex))
    data1=f.encrypt(base64.b64decode(data.encode()))
    #print(base64.b64encode(data1).decode())
    return base64.b64encode(data1).decode()
def dec(cipher,key_hex):
    f=Fernet(bytes.fromhex(key_hex))
    data=f.decrypt(cipher)
    b64data=base64.b64encode(data).decode()
    #print(b64data)
    return data
