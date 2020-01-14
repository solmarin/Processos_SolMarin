# Echo client program
import socket
import sys

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
data = s.recv(1024)
print(data)

while True:
    print >> sys.stderr, 'Introduce mensaje:'
    data = raw_input()
    s.sendall(data)
    t = s.recv(1024)
    print('Server-> mensaje renviado:',t)
    if(data=='Bye'): 
        data = s.recv(1024)
        print(data)
        break

s.close()
