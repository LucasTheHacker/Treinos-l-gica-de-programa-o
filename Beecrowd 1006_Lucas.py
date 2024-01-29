#Recebes 3 notas, com pesos 2, 3 e 5, respectivamente.
#Calcula a média ponderada e printa na tela
#1 digito de ponto flutuante

nota_1 = float(input()) #Possui peso 2
nota_1 = nota_1*2 #Atualizo o valor da variável com o peso dela 

nota_2 = float(input()) #Possui peso 3
nota_2 = nota_2*3 #Atualizo o valor da variável com o peso dela

nota_3 = float(input()) #Possui peso 5
nota_3 = nota_3*5 #Atualizo o valor da variável com o peso dela

media_ponderada = (nota_1 + nota_2 + nota_3)/10

print(f'MEDIA = {media_ponderada:.1f}')