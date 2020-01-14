# Echo server program
import socket
import time
import sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn,addr = s.accept()
while True:
    conn, sendall('Conectat')
    data = s.recv(1024)
    if data == 'Bye':
        time.sleep(1)
        break

conn.close()
s.close()
