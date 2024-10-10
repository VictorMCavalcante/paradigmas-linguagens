class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []

    def adicionar_empregado(self, empregado):
        self.empregados.append(empregado)

empresa = Empresa("Tech")
empregado1 = Empregado("Joao", "Desenvolvedor", 5000)
empregado2 = Empregado("Pedro", "Analista", 4000)
empresa.adicionar_empregado(empregado1)
empresa.adicionar_empregado(empregado2)
for empregado in empresa.empregados:
    print(f"{empregado.nome} - {empregado.cargo}: {empregado.salario}")
