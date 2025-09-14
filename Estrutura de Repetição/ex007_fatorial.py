n = int(input('Escolha um número?  '))
fatorial = 1
i = 1
while i <= n:
    fatorial = fatorial * i
    i += 1
print(f'O fatorial de {n} é {fatorial}')