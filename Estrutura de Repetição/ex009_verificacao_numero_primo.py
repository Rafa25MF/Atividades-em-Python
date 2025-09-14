n = int(input('Digite um número: '))
i = 2

while i < n and n % i != 0:
    i += 1

if n > 1 and i == n:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')