# Echo server program
import socket
import time
import sys
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

def rec(conn):
    while True:
        data = conn.recv(1024)
        print data
        if data == "Bye":
            break

def env(conn):
    while True:
        t = raw_input("---Server---")
        conn.sendall(t)

        if t == "Bye":
            conn.sendall(t)
            break

t1 = threading.Thread(target=env, args=(conn,))
t1.daemon = True
t1.start()

t2 = threading.Thread(target=rec, args=(conn,))
t2.start()

t2.join()

s.close()
