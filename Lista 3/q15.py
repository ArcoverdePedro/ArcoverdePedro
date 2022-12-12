n = int(input('Informe o numero: '))
aux = 0
cont = 1
cont2 = 0
while aux <= n:
    aux += cont 
    cont += 1
    if aux == n:
        print(f'{n} é um Triangular!')
        cont2 += 1
if cont2 == 0:
    print(f'{n} não é um Triangular!')