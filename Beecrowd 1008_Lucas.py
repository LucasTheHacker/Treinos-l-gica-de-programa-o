#Recebe 3 números: a identificação do funcionário, horas, valor/hora
#imprime a id_funci e horas*valor/hora com 2 pontos flututantes

id_funci = int(input())

horas_trab = int(input())

valor_hora = float(input())

print(f'NUMBER = {id_funci}')

print(f'SALARY = U$ {(horas_trab*valor_hora):.2f}') #ajuste de ponto flutuante
#tempo: 0.063s