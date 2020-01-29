# Echo client program
import socket
import sys
import threading

HOST = 'localhost'    # The remote host
PORT = 50009       # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

def env(s):
    while True:
        t = raw_input("Envia mensaje:")
        s.sendall(t)

        if t == "Bye":
            break


def rec(s):
    while True:
        data = s.recv(1024)
        print data

        if data == "Bye":
            s.sendall(data)
            break

t1 = threading.Thread(target=env, args=(s,))
t1.daemon = True
t1.start()

t2 = threading.Thread(target=rec, args=(s,))
t2.start()

t2.join()

s.close()
