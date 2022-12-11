n = int(input("Digite o valor de n: "))
aux = 0#auxiliar para a progressão aritimetica de segundo grau
raz = 1#razão da Pa de segundo grau
while aux <= n:
    aux = raz + aux
    raz +=1 
    #caso a PA seja igual ao N é triangular, mas se não for, não é triangular
    if aux == n:
        print(f"o numero {n} é triangular")
    else:
        print(f"o numero {n} não é triangular")