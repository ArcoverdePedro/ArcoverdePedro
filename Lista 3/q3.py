valor = int(input(" informe um valor "))
if valor <0:
    valor *= -1
if valor !=0:
    divisor = 1
    cnt = 0
    valor_1 = 1
    while valor_1 >= valor:
        while divisor <= valor_1:
            if valor_1 % divisor == 0:
                print (divisor,end=";")
                cnt+=1
            divisor +=1
        if cnt == 2:
            print("numero primo")
    valor_1 +=1
   