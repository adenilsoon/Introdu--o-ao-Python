def encontrar_elemento (elemento, array):
    encontrou = False
    
    for i in range(len(array)):
        if(array[i] == elemento):
            encontrou = True
            indice = i
        
    if(encontrou == False):
        print(f"{elemento} não foi encontrado em nossa base de dados :(")
    else:
        print(f"Encontramos {elemento} na posição {indice}")

clientes = ["Adenilson", "Júlia", "Garel do Mel", "Beatriz", "Arthur"]

print("=== BUSCAR CLIENTES ===\n")
elemento = str(input("Informe o nome do cliente: "))

print(encontrar_elemento(elemento, clientes))