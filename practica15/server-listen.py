# Echo server program
import socket
import time
import sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
while True:
    print >> sys.stderr, 'Conectado...'
    data = s.recv(1024)
    if data == 'Bye':
        time.sleep(1)
        break

s.close()
