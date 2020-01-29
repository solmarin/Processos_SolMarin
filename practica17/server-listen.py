from socket import socket, error
from threading import Thread

class Client(Thread):
    """
    Servidor eco - reenvia todo lo recibido
    """

    def __init__(self, conn, addr):
        Thread.__init__(self)

        self.conn = conn
        self.addr = addr

    def run(self):
        while True:
            try:
                input_data = self.conn.recv(1024)
            except error:
                print("Error de lectura")
                break
            else:
                if input_data:
                    self.conn.send(input_data)
def main():
    s = socket()

    s.bind(("localhost", 6030))
    s.listen(0)

    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("Conectado")
if __name__ == "__main__":
    main()
