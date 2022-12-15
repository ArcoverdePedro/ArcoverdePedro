a = int(input("determine um valor para a, diferente de 0: "))
b = int(input("determine um valor para b: "))
c = int(input("determine um valor para c: "))
#o valor de a deve ser diferente de 0
if a == 0:
    print("valor invalido")
    #o calculo de delta
else:
    delt = (b**2)-4*a*c
    #calculo do resto da equação 
    if delt < 0:
        print("valor de x não existe")
    elif delt == 0:
        print(f"o valor de x1 e x2 é {(-b+delt**2)/2*a}")
    else:
        print(f"o valor de x1 é {(-b+delt**2)/2*a} e o valor de x2 é {(-b-delt**2)/2*a}")