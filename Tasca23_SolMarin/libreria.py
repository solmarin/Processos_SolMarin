#-*- encoding: utf-8 -*-
import hashlib
import json
import base64
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64decode, b64encode
from Crypto.Util.Padding import unpad
from Crypto.Random import random
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto import Random

#MODUL 1
def GenerarKey():
    #RSAS
    key = RSA.generate(2048)
    return key

def ExKey(path, key):
    #Key
    keyEx = key.exportKey('PEM')
    #fichero
    fileEx = open(path+ ".pem", "wb")
    fileEx.write(keyEx)
    fileEx.close()


#MODUL 2
def GenerarKeySHA256():
    psswd = "8815"
    key = hashlib.sha256(psswd.encode("utf-8")).digest()
    return key

def EncriptarAES(path, key):
    #file
    file = open(path,"r")
    data = file.read()
    file.close()

    #key
    length = 16
    data = data + (length - len(data) % length) * chr(length - len(data) % length)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv = iv)
    Encriptado = cipher.encrypt(data.encode())

    return iv + Encriptado

def ImKey(path):
    return RSA.import_key(open(path).read())

def EncriptarKeyRSA(data,key):
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(data)

def SaveFile(path, key):
    fileExport = open(path+ ".txt", "wb")
    fileExport.write(key)
    fileExport.close()

#MODULO 3
def InKeyPri():
    #Key Privada (pem)
    key = input("Inserta Key: ")
    return key

def InKeyAES():
    #Key AES (txt)
    key = input("Inserta fichero Key AES: ")
    return key

def InMsjAES():
    #Msj Cifrado (txt)
    msj = input("Inserta fichero mensaje AES: ")
    return msj

def ImKeyPuPri(path):
    return RSA.import_key(open(path).read())

def DesRSA(msjEncriptado, key):
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(msjEncriptado)

def DesencriptaMsgAES(msjEncriptado,key):

    iv = msjEncriptado[:AES.block_size]
    msjExtraido = msjEncriptado[AES.block_size:]

    print("KEY:")
    print(key)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(msjExtraido).decode('utf-8')
