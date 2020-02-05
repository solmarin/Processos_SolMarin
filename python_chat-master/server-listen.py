# Echo server program
import socket
import time
import sys
clientes = []
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50010             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)


def conexiones(s):
    for c in clientes:
        c.close()

    del clientes[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)

            clientes.append(conn)

            print("Conexion establecida:" + conn[0])

        except:
            print("Error acceptar Conexion")


def rec(conn):
    while True:
        data = conn.recv(1024)
        if data == 'Bye':
            conn.sendall('Desconectat')
            time.sleep(1)
            break

def env():
    for c in clientes:
        clientes.conn.sendall(data)


t1 = threading.Thread(target=rec, args=(conn,))
t1.start()

t2 = threading.Thread(target=env, args=())
t2.start()



t1.join()

conn.close()

s.close()
