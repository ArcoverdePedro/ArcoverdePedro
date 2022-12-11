valor = int(input("informe um numero"))
if valor > 1:
    aux = 1
    while aux <= valor:
        cntdiv = 0
        div = 1
        while div <= valor:
            if aux %div == 0:
                cntdiv += 1
            if cntdiv >3: break
            div +=1
        if cntdiv==2:
            print(aux,end=",")
        aux+=1