binario = input('informe um número binário: ')
var1 = binario[::-1]
dec = 0
for cont in range(len(var1)):
    if var1[cont] == '1':
        dec += 2 ** cont
print(f'O valor decimal de {binario} é = {dec}')