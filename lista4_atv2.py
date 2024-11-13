def piramide_sequencial(n):
    for i in range(1, n + 1):
        text = ""
        for j in range(1, i + 1):
            text += str(j)
        print(text)

# Solicita a entrada do usuário
piramide = int(input("Digite um número: "))
piramide_sequencial(piramide)