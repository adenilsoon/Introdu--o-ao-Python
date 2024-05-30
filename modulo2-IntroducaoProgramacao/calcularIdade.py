numeroValido = False;
anoAtual = 2024;

while(numeroValido == False):

    nomeCompleto = str(input("Informe o seu nome completo: "));
    print("Informe o seu ano de nascimento: ");

    try:
        anoNascimento = int(input());

        if(anoNascimento >= 1922 and anoNascimento <= 2021):
            numeroValido = True;
            idade = anoAtual - anoNascimento;
            print("Nome: " + nomeCompleto);
            print("Idade: " + str(idade) + " anos");
        else:
            print("Você não informou um ano válido. Por favor tente novamente");

    except:
        print("Você digitou um caractere inválido")