valor = int(input(" informe um valor "))
if valor <0:
    valor *= -1
if valor !=0:
    divisor = 1
    while divisor <=valor:
        if valor % divisor == 0:
            print (divisor,end=";")
        divisor +=1