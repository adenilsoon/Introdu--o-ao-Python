def contarCaracteres():
    executando = True;

    while(executando):
        
        texto = input("Informe um texto ou palavra: ");
        opcao = int(input("Informe o número corresponde a informação que você forneceu acima: \n\n1 - Palavra\n2 - Texto\n3 - Sair\n\n>>> "));

        if(opcao == 1):
            totalCaracteres = len(texto);
            print("A palavra fornecida possui " + str(totalCaracteres) + " caracteres");
        
        elif(opcao == 2):
            palavras = texto.split();
            totalPalavras = len(palavras);
            print("O texto informado possui " + str(totalPalavras) + " palavras");
        elif(opcao == 3):
            executando = False
            print("Fechando programa...");
        else:
            print("\n\nDigite uma opção válida");
        
contarCaracteres();