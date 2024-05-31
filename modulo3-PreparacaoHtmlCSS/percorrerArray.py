#TODO Elaborar um sistema que imprime na tela na frente da loja os novos produtos que chegaram 
# Imprimir cada produto com a frase "Temos [produto] à venda!"

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'];

for i in range(len(lista_produtos)):
    print("Temos " + lista_produtos[i] + " à venda!");