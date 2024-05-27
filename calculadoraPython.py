# Calculadora com Python

num1 = int(input("Informe um número: "))
num2 = int(input("Informe um segundo número: "))

print("\n [ Utilize + para adição, - para subtração, * para multiplicação, / para divisão ]\n")
op = str(input("Conforme exemplos acima, informe o simbolo referente a operação matemática desejada: "))

print("\n")

def calcularNumeros(num1, num2, op):
    if(op == '+'):
        calculo = num1 + num2
        return calculo
    elif(op == '-'):
        calculo = num1 - num2
        return calculo
    elif(op == '*'):
        calculo = num1 * num2
        return calculo
    elif(op == '/'):
        calculo = num1 / num2
        return calculo
    elif(op != '+' and op != '-' and op != '*' and op != '/'):
        return 0

print(calcularNumeros(num1, num2, op))