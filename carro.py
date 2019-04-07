import veiculo

class Carro(veiculo.Veiculo):

    def __init__(self, cor, combustivel, quantidade_portas):
        super().__init__(cor, combustivel)
        self.quantidade_portas = quantidade_portas

    def quantidade_portas(self):
        print(f"Quantidade de portas: {self.quantidade_portas}")

    def detalhes_veiculo(self):
        super().detalhes_veiculo()
        print(f"Quantidade de portas: {self.quantidade_portas}")