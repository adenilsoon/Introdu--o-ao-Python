#TODO Atualizar array de produtos

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'];

# Imprimindo o array original
print(lista_produtos);

# Alterando o elemento do indíce 1
lista_produtos[1] = 'rímel';

# Alterando o elemento do indíce 4
lista_produtos[4] = 'cremes hidratantes';

# Removendo o último elemento do array 'delineadores'
lista_produtos.pop();

# Imprimindo o array atualizado
print(lista_produtos);
