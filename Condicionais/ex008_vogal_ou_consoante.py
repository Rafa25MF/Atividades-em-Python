letra = input('Digite uma letra: ')

vogal = 'a' or 'e' or 'i' or 'o' or 'u'

consoante = 'b' or 'c' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'm' or 'n' or 'p' or 'q' or 'r' or 's' or 't' or 'v' or 'w' or 'x' or 'y' or 'z'

if letra == vogal:
    print(f'A letra {letra} é uma vogal!')
elif letra == consoante:
    print(f'A letra {letra} é uma consoante')
else:
    print('Você não digitou uma letra!')

