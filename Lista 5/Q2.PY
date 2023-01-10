num = int(input('Informe um valor parar iniciar a P.A: '))
raz = float(input('Agora informe a razão da P.A: '))
qnt = int(input('Termos que quer encontrar na P.A? '))
pos = int(input(f'Posição a ser verificada\n(O Valor deve ser menor ou igual a {qnt}): '))
qnt = abs(qnt)
p_a=num
soma=0
cont=1
np=0
for x in range(cont,qnt+1): 
     print(p_a, end=' , ')
     soma = p_a + soma
     p_a+=raz
     cont+=1
     if cont == pos and pos <= qnt:
         np = p_a
print('P.A encerrada!')       
print(f'A soma da P.A é igual á {soma}!')
print(f'O número correspondente a {pos}° posição na P.A é = {np}!')
if raz > 0: print('P.A crescente!')
elif raz < 0: print('P.A descrescente!')
else: print('P.A constante!')