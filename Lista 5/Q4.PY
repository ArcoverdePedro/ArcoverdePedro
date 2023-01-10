valor = int(input('Informe um valor inteiro para verificar seu fatorial: '))
aux = valor
var = 1
fatorial = valor
if valor !=0:
    for x in range(1,valor):
        valor -= 1
        var = aux*valor 
        aux = var
    print (f'{fatorial}!= ',var)
else:
    print('Número informado é 0, portando, fatorial = 1')