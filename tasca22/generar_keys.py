import hashlib
import json
import base64
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from base64 import b64decode, b64encode
from Crypto.Util.Padding import unpad
from Crypto.Random import random
from Crypto import Random

def GenerarKey():
    key = RSA.generate(2048)
    return key

def ExportKeyEnPEM(path, key):
    k = key.exportKey('PEM')

    file_out = open(path+ ".pem", "wb")
    file_out.write(k)
    file_out.close()

def ImportKey(path):
    return RSA.import_key(open(path).read())

def EncriptarRSA(data,k):
    cipher = PKCS1_OAEP.new(k)
    return cipher.encrypt(data.encode())

def DesencriptarRSA(encryptedData, k):
    cipher = PKCS1_OAEP.new(k)
    return cipher.decrypt(encryptedData).decode('utf-8')


# ENCRIPTAR SHA256
def padding(s): return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def GenerarSHA256Key():
    password = input("INTRODUCE CLAVE: ")
    key = hashlib.sha256(password.encode("utf-8")).digest()
    return key

def EncriptarAES(data, k):

    #añadir padding al mensaje
    data = padding(data)

    #vector inicializacion
    iv = Random.new().read(AES.block_size)

    cipher = AES.new(k, AES.MODE_CBC, iv = iv)
    eData = cipher.encrypt(data.encode())

    return base64.b64encode(iv + eData)

# DESENCRIPTAR AES - CBC
def DesencriptarAESCBC(eData,k):

    eData = base64.b64decode(eData)

    #separación de la encriptacion
    iv = eData[:AES.block_size]
    encData = eData[AES.block_size:]

    cipher = AES.new(k, AES.MODE_CBC, iv)

    return cipher.decrypt(encData).decode('utf-8')
