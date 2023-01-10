plvr = input('Informe a palavra para verificarmos: ')
caixa = plvr.upper()
cont = ''
for pali in range(len(caixa)-1, -1, -1):
    cont += caixa[pali]
if cont == caixa:
    print(f'{plvr} é um palíndromo')    
else:
    print(f'{plvr} não é um palíndromo') 