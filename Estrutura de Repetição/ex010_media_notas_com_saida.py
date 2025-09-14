soma = 0
quantidade = 0
nota = float(input('Digite uma nota: '))

while nota >= 0:
    soma = soma + nota
    quantidade = quantidade + 1
    nota = float(input('Digite uma nota: '))

if quantidade > 0:
    media = soma / quantidade
    print(f'A média das notas é: {media}')
else:
    print('Você não digitou nenhuma nota válida')
