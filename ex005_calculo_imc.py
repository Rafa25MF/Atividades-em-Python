peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
mede = altura/100
imc = peso / (mede ** 2)
print(f'O seu IMC é: {imc:.4f}')

