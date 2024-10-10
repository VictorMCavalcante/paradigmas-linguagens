class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        return f"{self.ano} {self.marca} {self.modelo}"

carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2021)
carro3 = Carro("Ford", "Fiesta", 2019)

for carro in [carro1, carro2, carro3]:
    print(carro.exibir_detalhes())
