c = int(input('Digite o valor do Capital: '))
i = int(input('Digite qual foi o tempo investido: '))
t = int(input('Digite o valor da taxa do juros: '))
juros = (c * i * t) / 100 + c
print('O valor do investimento com juros é:', juros)