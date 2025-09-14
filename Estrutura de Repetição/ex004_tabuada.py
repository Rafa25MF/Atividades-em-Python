num = int(input('Digite um número: '))
numero = 1
print('\033[32m===========================================')
print('===               TABUADA               ===')
print('===========================================')
while numero <= 10:
    soma = num + numero
    print(f'A soma de: {num} + {numero} = {soma}')
    numero += 1
print('===========================================')