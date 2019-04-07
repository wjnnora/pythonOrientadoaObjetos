import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, cor, combustivel, quantidade_passageiro):
        super().__init__(cor, combustivel)
        self.quantidade_passageiros = quantidade_passageiro

    def quantidade_passageiros(self):
        print(f"Quantidade de passageiros: {self.quantidade_passageiros}")

    def detalhes_veiculo(self):
        super().detalhes_veiculo()
        print(f"Quantidade de passageiros: {self.quantidade_passageiros}")
