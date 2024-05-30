numPar = False;

while(numPar == False):
    print("Informe um número: ");

    try:
        numero = int(input());
        if(numero % 2 == 0):
            numPar = True;
            print("Você digitou um número par");
        else:
            print("O número que você digitou não é par. Por favor, digite novamente");
    except:
        print("Você inseriu um caracter inválido.")


