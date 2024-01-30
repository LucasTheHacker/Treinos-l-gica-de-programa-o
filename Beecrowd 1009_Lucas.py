#Recebe nome do vendedor, salário fixo, valor de vendas
#Imprime salário fixo + 15% do valor das vendas

nome = str(input())
salario_fixo = float(input())
vendas = float(input())
vendas = vendas * 0.15 #Atualiza vendas para a comissão que é do vendedor

print(f'TOTAL = R$ {(salario_fixo + vendas):.2f}')