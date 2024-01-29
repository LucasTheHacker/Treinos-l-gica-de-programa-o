'''Leia dois valores inteiros, no caso para variáveis A e B.
 A seguir, calcule a soma entre elas e atribua à variável SOMA. A seguir escrever o valor desta variável.
Entrada
O arquivo de entrada contém 2 valores inteiros.
Saída
Imprima a mensagem "SOMA" com todas as letras maiúsculas,
 com um espaço em branco antes e depois da igualdade seguido pelo valor correspondente à soma de A e B'''

A = int(input()) #A variável 'A' armazena esse valor

B = int(input()) #A variável 'B' armazena o segundo valor

print(f'SOMA = {A+B}') #Faço a conta diretamente na resposta, sem usar registradores intermediários. -> isso poupa tempo

#tempo 0.000 segundos