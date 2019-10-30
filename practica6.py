import time
from multiprocessing import Process

"""Funcio que mostra l'hora cada s segons"""
def t(s):
    while(True):
        print time.strftime("%X")
        time.sleep(s)
"""Funcio main on s'executen dos processos """
def main():
    p = Process(target=t, args=(1, ))
    p.start()
    for i in range(10):
        time.sleep(0.5)
        print (p.pid)
    p.terminate()
    print("fi")

if __name__ == '__main__':
    main()
