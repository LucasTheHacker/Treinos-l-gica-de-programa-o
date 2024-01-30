#Recebe código, quantidade e valor unit de duas peças.
#Output "VALOR A PAGAR: R$ x"

codigo_peca, quantidade_peca, valor_unit_peca = input().split(" ")
quantidade_peca = float(quantidade_peca)
valor_unit_peca = float(valor_unit_peca)

#Como fazer algo parecido com -- float(input.split) -- sem dar erro ???????

codigo_peca2, quantidade_peca2, valor_unit_peca2 = input().split(" ")
quantidade_peca2 = float(quantidade_peca2)
valor_unit_peca2 = float(valor_unit_peca2)

total = quantidade_peca*valor_unit_peca + quantidade_peca2*valor_unit_peca2
print(f'VALOR A PAGAR: R$ {total:.2f}')

#tempo = 0.080s