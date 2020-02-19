# Echo server program
import socket
import time
import sys
import threading
clientes = []
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50022               # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)
cliente = []

def rec(cliente):
    while True:
        data = cliente[0].recv(1024)
        if (data == 'Bye' or data == 'Bye\n' or data==''):
            data = "Desconectat\n"
            env(data,cliente)
            cliente[0].close()
            clientes.remove(cliente)
            break
            print("Conexion desconectada:" + str(cliente[0])+" - "+str(cliente[1]))

        t2 = threading.Thread(target=env, args=(data,cliente))
        t2.start()

def env(data, cliente):
    for c in clientes:
        if c!=cliente:
            c[0].sendall(str(cliente[1])+data)

def conexiones(s):
    while True:
        try:
            conn, address = s.accept()
            nombre = conn.recv(1024)

            if nombre.find('\n') !=-1:
                nombre = nombre[:(len(nombre)-1)]+": "

            cliente = (conn, nombre)
            clientes.append(cliente)
            print("Conexion establecida:"  + str(cliente[0])+" - "+str(cliente[1]))

            t1 = threading.Thread(target=rec, args=(cliente,))
            t1.start()

        except:
            print("Error acceptar Conexion")

t0 = threading.Thread(target=conexiones, args=(s,))
t0.start()
t0.join()
time.sleep(1)
s.close()
