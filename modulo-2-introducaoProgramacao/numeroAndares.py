# Imprimir andares, exceto o 13°, utilizando o FOR
for i in range(21, 0, -1):
   if (i != 13):
        print("Bem-Vindo ao " + str(i) + "° andar!")

print("\n")

# Imprimir andares, exceto o 13°, utilizando o WHILE
numeroAndar = 21
while(numeroAndar >= 1):
    if(numeroAndar != 13):
        print("Bem-Vindo ao " + str(numeroAndar) + "° andar!")
    numeroAndar-=1


    