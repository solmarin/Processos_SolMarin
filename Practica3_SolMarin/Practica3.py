class EquacioPrimerGrau:
    def __init__(self, eq):
        self.eq = eq

    def calcula(self):
        try:
            """ separamos por espacios para cojer las partes de la eq"""
            self.a, self.b, self.c, self.d,self.e = self.eq.split(" ")

            """eliminamos la x de la parte a"""
            self.A,self.restante = self.a.split("x")
        except:
            return("l'equacio no segueix el format: ax + b = c")

        try:
            self.A = float(self.A)
            self.c = float(self.c)
            self.e = float(self.e)
        except:
            return("l'equacio conte caracter no calculables: "+self.eq)

        """tratamos las partes"""
        if self.b == "+":
            self.a = float(self.e)-float(self.c)
            self.restante = float(self.a)/float(self.A)
            return float(self.restante)
        elif self.b == "-":
            self.a = float(self.c)+float(self.e)
            self.restante = float(self.a)/float(self.A)
            return float(self.restante)

        else:
            return("Operador no valid: "+ self.b)
