import random

key = random.randint(1, 100)
palpite = 0

while palpite != key:
    palpite = int(input('Tente adivinhar o número de 1 a 100: '))
    
    if palpite < key:
        print('Muito Baixo, PERDEU R$50,00')
    elif palpite > key:
        print ('Muito Alto. PERDEU R$100,00')
    else:
        print('Acertou. GANHOU R$0,001!!!')
    

