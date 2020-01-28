# Echo server program
import socket
import time
import sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
conn.sendall('Conectat')

while True:
    data = conn.recv(1024)
    print('Cliente -> mensaje enviado:',data)
    conn.sendall(data)
    if data == 'Bye':
        conn.sendall('Desconectat')
        time.sleep(1)
        break

conn.close()

s.close()
