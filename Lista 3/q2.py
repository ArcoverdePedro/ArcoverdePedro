valor = int(input(" informe um valor "))
if valor <0:
    valor *= -1
if valor !=0:
    divisor = 1
    cnt = 0
    while divisor <=valor:
        if valor % divisor == 0:
            print (divisor,end=";")
            cnt+=1
        divisor +=1
    if cnt == 2:
        print("numero primo")
    else:
        print("numero inteiro")
