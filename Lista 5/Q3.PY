valor = int(input('Informe o Valor inicial da P.G: '))
razao = float(input('Informe a Razão da P.G: '))
qnt = int(input('Quantos termos vc deseja encontrar: '))
posi = int(input(f'Informe a Posição do valor que você quer saber\n(A posição deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
prog = valor
cont = 1
nump = 0
soma = 0
for x in range(cont,qnt+1):
    print(f'{prog:.2f}', end = ' , ')
    soma = prog + soma
    prog *= razao
    cont += 1
    if cont == posi and posi <= qnt:
        nump = prog
print('P.G encerrada!')       
print(f'\nA soma da P.G é igual á {soma}!')
print(f'O número correspondente a {posi}° posição na P.G, é o = {nump}!')
if razao > 1:print('E Sua P.G é crescente!')
elif 0 < razao < 1:print('P.G descrescente!')
elif razao == 1: print('P.G constante!')
elif razao < 0: print('P.G oscilante!')
else: print('Insira um valor diferente de 0!')