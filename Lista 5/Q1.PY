decimal = int(input('Informe um valor inteiro: '))
binario = ''
for x in range(decimal+1):
    if decimal > 0:
        resto = decimal%2 
        decimal = decimal//2
        binario = str(resto) + binario   
print('O valor em binario é', binario)