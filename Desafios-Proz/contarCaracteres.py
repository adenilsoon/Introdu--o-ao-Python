def contarCaracteres():
    
    executando = True;

    while(executando):
        
        opcao = int(input("O que você deseja fazer:\n\n1 - Contar caracteres de uma palavra\n2 - Contar palavras de um texto\n3 - Sair do programa\n\n>>> "));
        print("\n")

        if(opcao == 1):
            texto = input("Informe uma palavra: ");
            totalCaracteres = len(texto);
            print("A palavra fornecida possui " + str(totalCaracteres) + " caracteres");
        
        elif(opcao == 2):
            texto = input("Informe um texto: ");
            palavras = texto.split();
            print("O texto informado possui " + str(len(palavras)) + " palavras");
        elif(opcao == 3):
            executando = False
            print("Fechando programa...");
        else:
            print("\n\nDigite uma opção válida");
        
contarCaracteres();