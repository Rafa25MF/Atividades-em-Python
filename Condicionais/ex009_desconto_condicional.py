valor = int(input('QUAL O VALOR DO PRODUTO? '))
            
rato = valor * 0.10
rato2 = valor - rato

if valor >= 100:
    print(f"O valor foi {valor} com 10% de desconto ele ira custar {rato2}")
