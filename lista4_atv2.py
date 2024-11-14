def sequencia(x):
    for i in range(1, x + 1):
        text = ""
        for lista in range(1, i + 1):
            text += str(lista)
        print(text)

piramide = int(input("Digite um número: "))
sequencia(piramide)