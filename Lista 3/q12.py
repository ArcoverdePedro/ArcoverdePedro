n = int(input('Insira um valor: '))
aux1 = 1
res = 0
n2 = 0
aux2 = aux1
#a sequencia de Fibonacci deve ser positiva e seŕa calculada a seguir
if n != 0:
    while aux1 <= n:
        res = aux2 + n2
        print(res, end=' ')
        aux1 +=1
        aux2 = n2
        n2 = res