#Calculadora de operação básica
num_um = int(input("Digite o primeiro número: "))
operador = int(input("Informe o operador(*, /, -, +): "))
num_dois = int(input("Digite o segundo número: "))

if operador == "*":
    resultado = num_um * num_dois
    print(resultado)
elif operador == "/":
    resultado = num_um / num_dois
    print(resultado)
elif operador == "-":
    resultado = num_um - num_dois
    print(resultado)
elif operador == "+":
    resultado = num_um + num_dois
    print(resultado)
else:
    print("Qualé parça, digita certo")