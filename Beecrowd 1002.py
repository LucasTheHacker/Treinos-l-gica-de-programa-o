#Este programa deve calcular a área de um círculo
#A entrada consiste em valor de ponto flutuante (dupla precisão), no caso, a variável raio.
#A fórmula é pi * raio^2 (Meramente matemática)
#Considera-se o valor de pi como 3.14159
# SAÍDA : Apresentar a mensagem "A=" seguido pelo valor da variável area, com 4 casas de ponto flutuante

pi = 3.14159 #Associo à variável pi o seu valor. (Não é necessário tipar pois o Python faz isso já)

Raio = float(input()) #Recebo a variável em ponto flutuante do usuário (por isso o uso do "float")

area_do_circulo = (pi * (Raio**2)) #Faço o cálculo da área e armazeno na variável area_do_circulo

print(f'A={area_do_circulo:.4f}') #coloco o f' (chamado de 'f string') e delimito 4 pontos de ponto flutuante