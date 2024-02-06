#Condicional.
# B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A - A//2 * A == 0
A, B, C, D = input().split()
inputs = [A, B, C, D] #transformo em lista pra tipar iterando os objetos.

for item in inputs:
    int(item)

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A - ((A//2)*2) == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")