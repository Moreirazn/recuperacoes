clientes_A = {"Alice", "Bob", "Charlie", "David"}
clientes_B = {"Charlie", "David", "Eve", "Frank"}

clientes_em_ambos = clientes_A and clientes_B
clientes_somente_A = clientes_A - clientes_B
clientes_apenas_um = clientes_A ^ clientes_B

clientes_unicos = len(clientes_A | clientes_B) - len(clientes_em_ambos)
total_cliente = len(clientes_A | clientes_B)
porcentagem_unicos = (clientes_unicos / total_cliente) * 100


print(f"Clientes em ambos os conjuynos: {clientes_em_ambos}")
print(f"Clientes apenas em clientes_A {clientes_somente_A}")
print(f"Clientes em apenas um conjunto: {clientes_apenas_um}")
print(f"A porcentagem de clientes únicos: {porcentagem_unicos}")