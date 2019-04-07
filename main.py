import carro, moto

carro = carro.Carro("vermelho", "flex", 4)
moto = moto.Moto("preto", "gasolina", 2)

carro.detalhes_veiculo()
print("")
moto.detalhes_veiculo()
print("")

carro.cor = "preto"
carro.combustivel = "gasolina"

carro.detalhes_veiculo()
print("")
moto.detalhes_veiculo()
print("")