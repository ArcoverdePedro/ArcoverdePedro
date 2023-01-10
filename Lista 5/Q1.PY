dec = int(input('Informe um valor inteiro: '))
bin = ''
for x in range(dec+1):
    if dec > 0:
        resto = dec%2 
        dec = dec//2
        bin = str(resto) + bin   
print('O valor em binario é', bin) 