"""
Programa que mostra els n primers nombres on n es introduida per teclat
"""
import sys
class llista_primers:
    """
    >>> llista_primers(3).llista
    [2, 3, 5]

    >>> llista_primers(4).llista
    [2, 3, 5, 7]
    """

    """
    llista tindra n nombres
    """

    def __init__(self, n):
        self.n = n
        self.llista = []
        self.busca()

    """
    Busca els n nombres primers amb l'operacio %
    """

    def busca(self):
        """
        Si la mida de llista es 0, s'introdueix 2.
        """

        if (len(self.llista) == 0):
            self.llista.append(2)
            self.busca()

            """
            Si la mida es mes gran que 0, es busquen els nombres primers.
            """

        elif (len(self.llista) < self.n):
            trobat = False
            seguent = self.llista[-1]+1
            while not trobat:
                for i in self.llista:
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent)
            self.busca()

"""
Tractem l'arxiu com arxiu principal
"""

if __name__ == '__main__':
    #import doctest
    l = llista_primers(int(sys.argv[1]))
    print l.llista
    #doctest.testmod()
