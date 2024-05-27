qntDeRodas = int(input("Digite a quantidade de rodas do veículo: "))
pesoBruto = int(input("Digite o peso bruto em quilogramas: "))
qntDePessoas = int(input("Digite a quatidade de pessoas no veículo?: "))

if (qntDeRodas >= 2) and (qntDeRodas <= 3):
    print("Sua habilitação é A")
if (qntDeRodas == 4) and (qntDePessoas <= 8) and (pesoBruto <= 3500):
    print("Sua habilitação é B")
if (qntDeRodas >= 4) and (pesoBruto >= 3500) and (pesoBruto <= 6000):
    print("Sua habilitação é C")
if (qntDeRodas >= 4) and (qntDePessoas >= 8):
    print("Sua habilitação é D")
if (qntDeRodas >= 4) and (pesoBruto > 6000):
    print("Sua habilitação é E")