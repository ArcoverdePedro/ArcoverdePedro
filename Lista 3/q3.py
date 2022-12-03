valor = int(input(" informe um valor "))
if valor <0:
    valor *= -1
if valor !=0:
    cnt = 0
    valor_1 = 1
    while valor_1 <= valor:
        divisor = 1
        while divisor <= valor_1:
            if valor_1 % divisor == 0:    
                cnt+=1    
                divisor +=1
            if cnt == 2:
                print(f"o numero {valor_1} é primo")
            valor_1 +=1    
           
