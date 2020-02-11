# Echo server program
import socket
import time
import sys
import threading
clientes = []
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50017               # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)

def rec(conn):
    while True:
        data = conn.recv(1024)
        if (data == 'Bye' or data == 'Bye\n'):
            if conn in clientes:
                clientes.pop(clientes.index(conn))
            print("Conexion desconectada:" + str(conn))


        t2 = threading.Thread(target=env, args=(data,conn))
        t2.start()



def env(data, conn):
    for c in clientes:
        if c!=conn: c.sendall(data)

def conexiones(s):
    while True:
        try:
            conn, address = s.accept()
            clientes.append(conn)
            print("Conexion establecida:" + str(conn))

            t1 = threading.Thread(target=rec, args=(conn,))
            t1.start()

        except:
            print("Error acceptar Conexion")

t0 = threading.Thread(target=conexiones, args=(s,))
t0.start()
t0.join()
time.sleep(1)
s.close()
