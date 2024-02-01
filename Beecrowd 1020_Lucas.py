#converte dias pra meses anos e dias
#segue o mesmo raciocínio do beecrowd 1018

dias = int(input())

anos = dias//365
dias -= anos*365

meses = dias//30
dias -= meses*30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')