import abc

class Veiculo(abc.ABC):
    def __init__(self, cor, combustivel):
        self.__cor = cor
        self.__combustivel = combustivel

    def __del__(self):
        """Implementação básica de um destrutor em Python"""
        print("O objeto foi removido da memória")

    @property
    def cor(self):
        print(f"Cor do veículo: {self.__cor}")

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def combusitvel(self):
        print(f"Tipo de combustível: {self.__combustivel}")

    @combusitvel.setter
    def combustivel(self, combustivel):
        self.__combustivel = combustivel

    @abc.abstractmethod
    def detalhes_veiculo(self):
        print(f"Cor: {self.__cor}")
        print(f"Combustível: {self.__combustivel}")