# Echo client program
import socket
import sys

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST,PORT))
while True:
    print >> sys.stderr, 'Introduce palabras:'
    data = raw_input()
    s.sendall(data)
    if(data=='Bye'): break
s.close()
