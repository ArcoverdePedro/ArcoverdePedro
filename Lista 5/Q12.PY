NUMB1 = int(input('Insira o primeiro número: '))
NUMB2 = int(input('Insira o segundo número: '))
MAR, menor = NUMB1, NUMB2
nums,cont = '', 2
for cont in range(100):
    if MAR == 1 or menor == 1: break
    if MAR % cont == 0 and menor % cont ==0:
        nums += str(cont)
        MAR //= cont
        menor //= cont
    else:
        if MAR % cont == 0 or menor % cont == 0:
            if MAR % cont == 0: MAR //= cont
            elif menor % cont == 0: menor //= cont
        else: cont +=1 
multiplicação = 1
for num in nums : multiplicação *= int(num)
print(f'O maior divisor comum de {NUMB1} e {NUMB2} é {multiplicação}.')