def classificarProduto():
    
    nomeProduto = str(input("Digite o nome do produto: "));
    precoProduto = float(input("Informe o valor do produto: "));

    try:
        if(precoProduto < 50):
            print(nomeProduto + " é classificado com BAIXO");
        elif(precoProduto >= 50 and precoProduto <= 100):
            print(nomeProduto + " é classificado como MÉDIO");
        elif(precoProduto > 100):
            print(nomeProduto + " é classificado como CARO");
    except:
        print("Informe um nome e um valor válido para o produto.");

classificarProduto();

