import sys
from libreria import *

#key "entera"
key = GenerarKey()

#Key privada
ExKey("SolMarin_Privada", key)

#Key publica
ExKey("SolMarin_Publica", key.publickey())
