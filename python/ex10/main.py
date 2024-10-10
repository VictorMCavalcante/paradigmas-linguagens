class Calculadora:
    @staticmethod
    def somar(a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

print(Calculadora.somar(2, 3))       
print(Calculadora.somar(2, 3, 4))   
