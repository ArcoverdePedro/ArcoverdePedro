vi = int(input('Qual o primeiro valor da PA? '))
r = float(input('Razão da PA: '))
qnt = int(input('Quantidade de numeros na PA: '))
qnt = abs(qnt)
p = int(input('Em que posição você deseja saber o valor da pa: '))
vpa=vi
soma=0
cont=1
numposi=0
#a seguir está o calculo da PA, 
while cont <= qnt:
     print(vpa, end=' , ')
     soma = vpa + soma
     vpa+=r
     cont+=1
     if cont == p and p <= qnt:
         numposi = vpa     
print(f'A soma dos termos é igual a {soma}')
print(f'O número correspondente a {p}° Posição na P.A, é o {numposi}!')
if r > 0: print('E Sua P.A é crescente!')
elif r < 0: print('E Sua P.A é Descrescente!')
else: print('E Sua P.A é constante!')