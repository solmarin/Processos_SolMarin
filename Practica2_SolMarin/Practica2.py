"""
Practica 2: Solucionador d'equacions de primer grau
    Escriu un programa python que solucioni una equacio de primer grau del tipus ax + b = c. L'equacio arriba en forma d'String
    Cal que programis una classe EquacioPrimerGrau amb un sol metode calcula(String equacio)
    Aquesta classe s'encarregara d'extreure cada element de l'aquacio:
        a = part1
        b = part2
        operador
        c = part3
"""

class EquacioPrimerGrau:
    def __init__(self, eq):
        self.eq = eq

    def calcula(self):
        """ separamos por espacios para cojer las partes de la eq"""
        self.a, self.b, self.c, self.d,self.e = self.eq.split(" ")

        """eliminamos la x de la parte a"""
        self.A,self.restante = self.a.split("x")

        """tratamos las partes"""
        if self.b == "+":
            self.a = float(self.e)+float(self.c)
        else:
            self.a = float(self.e)-float(self.c)

        self.restante = float(self.a)/float(self.A)

        print float(self.restante)
