#Nível 6
#Reaproveitando o código e a lógica do beecrowd 1018
#Recebe um valor de ponto flutuante de dupla precisão e devolve a quantidade mínima de notas e moedas que representam aquele valor

valor = float(input())
valor_moedas = valor - (valor//1) #pego apenas o valor flutuante
valor =  valor//1  #transformo pra inteiro somente pra facilitar os cálculos
valor = int(valor)
nota_100 = valor//100  #o operador // pega a parte inteira de uma divisão
valor -= (valor//100)*100 #atualizo a variável diminuindo o valor que ja foi contado em cédulas de 100.

#repito esse processo nos outros

nota_50 = valor//50
valor -= (valor//50)*50

nota_20 = valor//20
valor -= (valor//20)*20

nota_10 = valor//10
valor -= (valor//10)*10

nota_5 = valor//5
valor -= (valor//5)*5

nota_2 = valor//2
valor -= (valor//2)*2

moeda_100 = valor  #só pode ser 1, quando tiver.

print("NOTAS:")
print(f'{nota_100} nota(s) de R$ 100.00')
print(f'{nota_50} nota(s) de R$ 50.00')
print(f'{nota_20} nota(s) de R$ 20.00')
print(f'{nota_10} nota(s) de R$ 10.00')
print(f'{nota_5} nota(s) de R$ 5.00')
print(f'{nota_2} nota(s) de R$ 2.00')

moeda_050 = valor_moedas//0.5
valor_moedas -= moeda_050 * 0.5
   
moeda_025 = valor_moedas//0.25
valor_moedas -= moeda_025 * 0.25

moeda_010 = valor_moedas//0.1
valor_moedas -= moeda_010 * 0.1

moeda_005 = valor_moedas//0.05
valor_moedas -= moeda_005 * 0.05

moeda_001 = valor_moedas/0.01  #Mudei de // pra / e funcionou

print("MOEDAS:")
print(f'{moeda_100:.0f} moeda(s) de R$ 1.00')
print(f'{moeda_050:.0f} moeda(s) de R$ 0.50')
print(f'{moeda_025:.0f} moeda(s) de R$ 0.25')
print(f'{moeda_010:.0f} moeda(s) de R$ 0.10')
print(f'{moeda_005:.0f} moeda(s) de R$ 0.05')
print(f'{moeda_001:.0f} moeda(s) de R$ 0.01') 

#print(0.03//0.01) PROBLEMA IDENTIFICADO
'''Por algum motivo, o python pega o valor inteiro da divisão acima
como 2, de forma que é necessário fazer a divisão simples e converter pra inteiro.'''
