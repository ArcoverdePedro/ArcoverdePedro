a=int(input("valor do lado a "))
b=int(input("valor do lado b "))
c=int(input("valor do lado c "))
#checando se é um triangulo de fato
if a <= 0 or b<=0 or c<=0 or a + b < c or b + c < a or a + c < b:
    print("valores invalidos")
else:
    #classificação dos triangulos
    if a == b and b == c:
        print("Triângulo equilatero")
    elif a != b and b !=c and a!=c:
        print("Triângulo escaleno")
    else:
        print("Triângulo isoceles")