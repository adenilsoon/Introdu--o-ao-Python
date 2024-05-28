# Criação de um array
lista = ["Adenilson", 22, 1.70, False]

print(lista)

# Apresentar o primeiro elemento
print(lista[0])

# Imprimir a quantidade de elementos do array
print(len(lista))

# Deletando o último elemento
lista.pop()
print(lista)

# Buscar um elemento em um array
def achar_elemento(elem, arr):
    achou = False
    
    for i in range(len(arr)):
        if(arr[i] == elem):
            achou = True

    if(achou == False):
        print(elem + " não foi encontrado :(")
    else:
        print("Achamos o elemento: " + elem)

nomes = ["Adenilson", "Wytam Gabriel", "Lucas", "Arthur"]
achar_elemento("Lucas", nomes)