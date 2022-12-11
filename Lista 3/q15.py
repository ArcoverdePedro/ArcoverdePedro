n = int(input("Digite o valor de n: "))
aux = 1
while aux * (aux+1) * (aux+2) <= n:
    aux = aux + 1
if aux * (aux+1) * (aux+2) == n:
    print(f"o numero {n} é triangular")
else:
    print(f"o numero {n} não é triangular")