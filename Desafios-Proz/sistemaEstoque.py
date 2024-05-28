import time

# Descrição do produto, marca, tamanho, quantidade em estoque
def manipular_estoque(arr):
    fechar = False

    while(fechar == False):
        print("\nEscolha uma opção. Digite o número correspondente")
        print("\n1. Ver produtos em estoque\n2. Adicionar novo produto\n3. Alterar produto\n4. Fechar o sistema")
        acao = input("\n>>> ")

        if(acao == "1"):
            print("\n=== PRODUTOS EM ESTOQUE ===\n")
            for i in range(len(arr)):
                print(str(i) + " - " + arr[i])
                if(i == len(arr)):
                    print("===========================\n")
        elif(acao == "2"):
            print("Qual o novo produto a ser adicionado?")
            novoProduto = input(">>> ")

            arr.append(novoProduto)
            print("O produto " + novoProduto + " foi adicionado com sucesso!")

        elif(acao == "3"):
            print("Qual o índice do produto que você deseja alterar?")
            indice = int(input(">>> "))
            print("Qual o novo produto a ser adicionado?")
            novoProduto = input(">>> ")
            arr[indice] = novoProduto
            print("O produto " + novoProduto + " foi adicionado com sucesso!")
        
        elif(acao == "4"):
            print("\nAtualizando base de dados...")
            time.sleep(3)
            print("Encerrando sistema...")
            time.sleep(2)
            print("Sistema encerrado.\n")
            fechar = True

        else:
            print("!!! Por favor informe um número válido !!!")
    
produtos = ["Óleo de Cozinha", "Leite Itambé", "Macarrão Instantâneo", "Ovos branco", "Biscoito PassaTempo"]

manipular_estoque(produtos)