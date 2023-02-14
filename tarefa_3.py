

class carro:
     def __init__(self, cor, placa, modelo):
        self.cor = cor
        self.placa = placa
        self.modelo = modelo

carro1 = carro("vermelho", "ABC-1234", "Fusca")
carro2 = carro("preto", "DEF-5678", "Civic")
carro3 = carro("azul", "GHI-9101", "Palio")
carro4 = carro("branco", "JKL-2345", "Gol")
carro5 = carro("prata", "MNO-6789", "Corsa")
carro6 = carro("verde", "PQR-0123", "Fit")
carro7 = carro("amarelo", "STU-3456", "HB20")
carro8 = carro("cinza", "VWX-7890", "Onix")
carro9 = carro("marrom", "YZA-1235", "Uno")
carro10 = carro("laranja", "BCD-6789", "Up")

lista_carros = [carro1, carro2, carro3, carro4, carro5, carro6, carro7, carro8, carro9, carro10]

def consulta(placa):
    for carro in lista_carros:
        if carro.placa == placa:
            print("Cor:", carro.cor)
            print("Placa:", carro.placa)
            print("Modelo:", carro.modelo)
            return
        print("Carro não encontrado.")


placa = input("Digite a placa do carro que deseja consultar: ")


consulta(placa)