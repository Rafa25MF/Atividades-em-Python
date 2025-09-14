for rafa in range (0, 1000000000):

    idade = int(input('Qual é sua idade: '))

    if idade < 0:
        print('VOCÊ NÃO EXISTE!')
    elif idade >= 0 and idade <= 2:
        print('Você é um bebê!')
    elif idade >= 3 and idade <= 12:
        print('Você é uma criança!')
    elif idade >= 13 and idade <= 17:
        print('Você é um adolecente!')
    elif idade >= 18 and idade <=24:
        print('Você é um adulto jovem!')
    elif idade >= 25 and idade <= 59:
        print('Você é um adulto')
    elif idade >= 60:
        print('Você é um indoso')
    elif idade >= 200:
        print('Era para você está MORTO ou você é um ALIENIGENA!!!!')