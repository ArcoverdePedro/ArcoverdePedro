palavra = input('Informe a palavra para verificarmos: ')
caixa = palavra.upper()
contador = ''
for palindromo in range(len(caixa)-1, -1, -1):
    contador += caixa[palindromo]
if contador == caixa:
    print(f'{palavra} é um palíndromo')    
else:
    print(f'{palavra} não é um palíndromo')