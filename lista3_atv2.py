#Contar todos os números primos até o num x
contador = int(input("Digite o número limite para a contagem: "))

for num_primo in range(1, contador + 1):
    for num_prim_divisor in range(2, int(num_primo ** 0.5) + 1):
        if num_primo % num_prim_divisor == 0:
            print(f"O número: {num_primo} não é primo")
            break
    else:
        print(f"O número: {num_primo} é primo")