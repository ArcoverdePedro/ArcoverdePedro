num = int(input('Valor inicial: '))
quo = float(input('Razão: '))
qnt = int(input('Termos a serem encontrados: '))
pos = int(input(f'Posição a ser encontrada: \n(O Valor deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
prog = num
cont = 1 
nump = 0
soma = 0
for x in range(cont,qnt+1):
    print(f'{prog:.2f}', end = ' , ')
    soma = prog + soma
    prog *= quo
    cont += 1
    if cont == pos and pos <= qnt:
        nump = prog
print('P.G encerrada!')       
print(f'\nA soma da P.G é igual á {soma}!')
print(f'O número correspondente a {pos}° posição na P.G, é o = {nump}!')
if quo > 1:print('P.G crescente!')
elif 0 < quo < 1:print('P.G descrescente!')
elif quo == 1: print('P.G constante!')
elif quo < 0: print('P.G oscilante!')
else: print('valor deve ser diferente de 0!')