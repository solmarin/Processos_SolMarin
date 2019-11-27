from datetime import datetime
from multiprocessing import Pool
def primers(num):
    for i in range(2, num/2):
        if num % i == 0:
            return False
        else:
            return True

if __name__ == '__main__':
#indicamos los processos que queremos ejecutar a la vez y en que rango ( en este caso 100)
    pool = Pool(processes=5)
    range = range(40000000, 40000100)
#Contador de tiempo en que tarda en hacer cada proceso
    start = datetime.now()
    it = pool.imap(primers, range)
    i = 0
    m = 40000000
#bloque para controlar los decimales del numero (tiempo)
    while(i<50):
        print str(m), str(it.next())
        m+=1
        i+=1
#Mostrar el tiempo total de todos los procesos
    print datetime.now() - start

#TIEMPOS FINALES
#10 [0:37.811796]
#5 [0:00:47.303910]
#2 [0:00:47.815318]
