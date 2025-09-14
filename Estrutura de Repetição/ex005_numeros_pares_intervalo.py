inicio = int(input("primeiro número: "))
fim = int(input("segundo número: "))

if inicio > fim:
    inicio, fim = fim, inicio


print ("Os número pares são:")
while inicio < fim:
    if inicio % 2 == 0:
        print (inicio)
    inicio += 1




