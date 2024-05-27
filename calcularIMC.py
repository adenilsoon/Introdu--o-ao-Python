print("CALCULAR IMC\n")

peso = int(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

def calcularIMC(peso, altura):
    imc = peso/(altura * altura)
    return imc

resultado = calcularIMC(peso, altura)

if(resultado <= 18.5):
    print("\nO seu indíce de massa corporal é " + str(resultado))
    print("Você está com o status de MAGREZA")
elif(resultado > 18.5 and resultado <= 24.9):
    print("\nO seu indíce de massa corporal é " + str(resultado))
    print("Você está com o status de SAUDÁVEL")
elif(resultado >= 25 and resultado <= 29.9):
    print("\nO seu indíce de massa corporal é " + str(resultado))
    print("Você está com o status de SOBREPESO")
elif(resultado > 30 and resultado <= 34.9):
    print("\nO seu indíce de massa corporal é " + str(resultado))
    print("Você está com o status de OBESIDADE GRAU I")
elif(resultado > 35 and resultado <= 39.9):
    print("\nO seu indíce de massa corporal é " + str(resultado))
    print("Você está com o status de OBESIDADE SEVERA GRAU Ii")
else:
    print("Você está com o status de OBESIDADE MORBIDA GRAU III")
