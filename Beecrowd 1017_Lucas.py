#automóvel de 12km/l
# (A * B)/12

horas = int(input()) #análise dimensional --- horas

velocidade = int(input()) #análise dimensional --- km/h

litros = (horas * velocidade)/12 #(h * km/h)/12km/L --> LITROS

print(f'{litros:.3f}')