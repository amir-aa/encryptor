from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from cryptography.fernet import Fernet
import logging,base64
from funcs import *
app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

def encrypt_data(data: bytes, key: bytes) -> str:
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    return encrypted_data.decode('utf-8')


def decrypt_data(encrypted_data: bytes, key: bytes) -> bytes:
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

@app.post("/encrypt/")
async def encrypt_bytes(data: dict) -> str:
    try:

        key = data['key']
        encoded_data = data['data'].encode()

        encrypted_data = enc(base64.b64encode(encoded_data).decode(), key)
        resp={"cipher":encrypted_data}
        return JSONResponse(resp)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/decrypt/")
async def decrypt_bytes(data: dict) -> str:
    try:
 
        key =data['key']
        encoded_data = data['data'].encode()
        
     
        encrypted_data = base64.b64decode(encoded_data)

        decrypted_data = dec(encrypted_data, key)
        resp={"Plaintext":decrypted_data.decode('utf-8')}
        return JSONResponse(resp)
    except Exception as e:
        with open("logs.txt",'a') as f:
            f.write(str(e))
        raise HTTPException(status_code=400, detail=str(e))
    

@app.post("/v1/key/")
async def keygen1() :
    resp= {'key':generateKey()}
    return JSONResponse(resp)
