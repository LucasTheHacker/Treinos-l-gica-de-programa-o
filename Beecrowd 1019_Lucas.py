#recebe segundos e transforma em horas, minutos e segundos
#1h tem 3600s 
#1 min tem 60s
#Segue a mesma lógica da atualização de variável do Beecrowd 1018_Lucas.py

tempo_segundos = int(input())

horas = tempo_segundos//3600
tempo_segundos -= horas*3600

minutos = tempo_segundos//60
tempo_segundos -= minutos * 60

print(f'{horas}:{minutos}:{tempo_segundos} ')