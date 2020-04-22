import sys
from libreria import *

#key sha256
txt = str(sys.argv[2])
key = str(sys.argv[1])

KeySHA256 = GenerarKeySHA256()

#Encriptar fichero con AES (mensaje.txt)
EncriptadoAES = EncriptarAES(txt, KeySHA256)

#Xifrar la clau AES amb la clau RSA pública. (SolMarin_Publica.pem)
keyPub = ImKey(key)
keyEncriptadaAES = EncriptarKeyRSA(KeySHA256, keyPub)

#Guardamos el mensaje encriptado en AES + vi
SaveFile("missatge_en", EncriptadoAES)

#Guardamos key AES encriptada en RSA Privada
SaveFile("en_k_aes",keyEncriptadaAES)
