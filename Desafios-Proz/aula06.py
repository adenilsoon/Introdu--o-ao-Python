# def é utilizado para definir uma função em Python
def mostrarNumero():

    numero_valido = False

    while(numero_valido == False): 
        try:
            print("Escreva um número maior que 0: ")
            num = int(input())

            if(num > 0):
                
                print("Você escolheu o número: " + str(num))
                numero_valido = True
            else:
                print("Você digitou um número maior que 0")
        except:
                print("Você precisa digitar um número válido")

# mostrarNumero()

# Verificar se é divísivel por 2 e por 3
def verificarDivisao():
     
            print("Escreva um número: ")
            num = int(input())

            if(num % 2 == 0 and num % 3 == 0):
                print("O número " + str(num) + " informado por você é divísivel por 2 e 3!")
                numero_valido = True
            else:
                print("O número " + str(num) + " informado por você NÃO é divísivel por 2 e 34")
        

verificarDivisao()
