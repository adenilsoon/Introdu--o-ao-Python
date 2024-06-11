def contarCaracteres():
    
    executando = True;
    
    try:
        while(executando):
            
            opcao = int(input("\nO que você deseja fazer:\n\n1 - Contar caracteres de uma palavra\n2 - Contar palavras de um texto\n3 - Sair do programa\n\n>>> "));

            if(opcao == 1):
                texto = input("Informe uma palavra: ");
                totalCaracteres = len(texto.replace(" ",""));
                print("A palavra fornecida possui " + str(totalCaracteres) + " caracteres");
            
            elif(opcao == 2):
                texto = input("Informe um texto: ");
                palavras = texto.split();
                print("O texto informado possui " + str(len(palavras)) + " palavras");
            elif(opcao == 3):
                executando = False
                print("Fechando programa...");
            else:
                print("\nDigite uma opção válida");
    except: 
        print("\nInformação inválida, tente novamente\n");   
contarCaracteres();