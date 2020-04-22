import sys
from libreria import *

#key Privada (SolMarin_Privada.pem)
KeyPem = str(sys.argv[1])

#"en_k_aes.txt" + key privada (AES cifrada)
txtAES = open(str(sys.argv[2]),'rb').read()

#"missatge_en.txt" (mensaje cifrado en  AES)
txtMsj = open(str(sys.argv[3]),'rb').read()

#importa  Key privada
keyPri = ImKeyPuPri(KeyPem)

#muestra la key privada
print("Key Privada: " + str(keyPri))


#Desencripta: key AES con Key Privada
claveAES = DesRSA(txtAES,keyPri)

mensaje = DesencriptaMsgAES(txtMsj, claveAES)

print ("Mensaje:" + mensaje)
