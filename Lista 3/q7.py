val = int(input("Informe o Valor inicial da P.G: "))
q = float(input("Informe a Razão da P.G: "))
qnt = int(input("Quantos termos vc deseja encontrar? "))
pos = int(input(f"qual posição deseja saber? "))
qnt = abs(qnt)
Pg = val
cont = 1
numpos = 0
soma = 0
if val != 0 and qnt != 0 and q != 0:
    while cont <= qnt:
        print(f"{Pg:.2f}", end = " , ")
        soma = Pg + soma
        Pg *= q
        cont += 1
        if cont == pos and pos <= qnt:
            numpos = Pg       
    print(f"A soma da P.G é igual á {soma}")
    print(f"O número correspondente a {pos}° posição na P.G, é o {numpos}")
    if q > 1: print("E Sua P.A é crescente!")
    elif 0 < q < 1: print("E Sua P.A é Descrescente!")
    elif q == 1: print("E Sua P.A é constante!")
    else: print("E Sua P.A é oscilante!")
else: print("O valor diferente de 0!")