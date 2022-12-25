plva1 = input('Informe a Primeira Palavra do Anagrama: ')
plva2 = input('Informe a Segunda Palavra do Anagrama: ')
var1, var2 = plva1.upper(), plva2.upper()
if len(plva1) == len(plva2):
    cont = 0
    cont1 = 1
    cont2 = 1
    cont3 = 1
    ultd = var1[-1] in var2 and var2[-1] in var1
    while cont1 < len(plva2):
        anagrama = var2.find(var1[cont:cont2])
        cont+=1
        cont1 += 1
        cont2 += 1
        if anagrama != -1 and ultd == True:
             cont3 += 1 
    if cont3 == len(plva2):
        print(f'Sua palavra é um anagrama')
    else:
        print(f'{plva1} Não é Anagrama de {plva2}')
else:
    print(f'{plva1} Não é Anagrama de {plva2}')