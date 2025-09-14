n = int(input('Qual número você quer ver a sequencia? '))
a = 1
b = 1

i = 1
while i < n:
    proximo = a + b
    print(proximo)
    a = b
    b = proximo
    i += 1
