NUMB1 = int(input('Insira o primeiro número: '))
NUMB2 = int(input('Insira o segundo número: '))
MAR, menor = NUMB1, NUMB2
nums,contador = '', 2
for contador in range(100):
    if MAR == 1 or menor == 1: break
    if MAR % contador == 0 and menor % contador ==0:
        nums += str(contador)
        MAR //= contador
        menor //= contador
    else:
        if MAR % contador == 0 or menor % contador == 0:
            if MAR % contador == 0: MAR //= contador
            elif menor % contador == 0: menor //= contador
        else: contador +=1
multiplicação = 1
for num in nums : multiplicação *= int(num)
print(f'O maior divisor comum de {NUMB1} e {NUMB2} é {multiplicação}.')