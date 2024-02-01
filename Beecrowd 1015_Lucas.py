#Recebe x1, y1
#Recebe x2, y2
#Output da distância entre esses dois pontos

x1, y1 = input().split()
x1 = float(x1)
y1 = float(y1)

x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)

distancia = (((x1 - x2)**2 + (y1 - y2)**2)**0.5)

print(f'{distancia:.4f}}')
#tempo = 0.147s
#tempo com conta no print = 0.183s