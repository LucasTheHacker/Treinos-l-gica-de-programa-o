'''Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno.
 A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11).
 Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.'''

#Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade.

nota_A = float(input()) #recebe a primeira nota, que tem peso 3.5
#Soma dos pesos = 11
nota_B = float(input()) #recebe a segunda nota, que tem peso 7.5

media_ponderada = ((nota_A*3.5)+(nota_B*7.5))/11

print(f'MEDIA = {media_ponderada:.5f}')

#TEMPO:0.092s