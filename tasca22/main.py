from generar_keys import *

#RSA

#generamos la llave
key = GenerarKey()
print(key.exportKey())

#exportando las llaves a ficheros
ExportKeyEnPEM("privada_key", key)
ExportKeyEnPEM("publica_key", key.publickey())

#importamos llave
privada_key = ImportKey("privada_key.pem")
print("PRIVATE KEY:" + str(privada_key))
publica_key = ImportKey("publica_key.pem")
print("PUBLIC KEY:" + str(publica_key))

#encriptar mensaje
eData = EncriptarRSA('ESTO ES UN EJEMPLO DE MENSAJE, PONME UN 10.', publica_key)
print(str(eData))

#desencriptar mensaje
dData = DesencriptarRSA(eData,privada_key)
print("MENSAJE: " + str(dData))

#SHA256

#generar llave
sha256_Key = GenerarSHA256Key()
print(sha256_Key)

#encriptar mensaje con una "llave adjuntada" ( o tienes todo el mensaje o no tienes nada)
eSHA256Data = EncriptarAES('ESTO ES UN SEGUNDO EJEMPLO DE MENSAJE, PONME UN 10.', sha256_Key)
print("IV + MENSAJE : " + str(eSHA256Data))
#desencriptar mensaje con una "llave adjuntada" ( o tienes todo el mensaje o no tienes nada)
dData = DesencriptarAESCBC(eSHA256Data , sha256_Key)
print("MENSAJE: " + dData)
