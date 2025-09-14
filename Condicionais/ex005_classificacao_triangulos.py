lado1 = float(input('Fale o primeiro lado do triângulo? '))
lado2 = float(input('Fale o primeiro lado do triângulo? '))
lado3 = float(input('Fale o primeiro lado do triângulo? '))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):

    if lado1 == lado2 == lado3:
        print('É um triângulo equilatero (todos os lados são iguais)')
    elif lado1 == lado2 or lado1 == lado3:
        print('É um triângulo isósceles (dois os lados são iguais)')
    else:
        print('É um triângulo escaleno (todos os lados são diferentes)')

else:
    print('Os valores informados não formam um triângulo.')

