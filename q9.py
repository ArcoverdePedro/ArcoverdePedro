a = float(input("primeiro angulo do triangulo "))
b = float(input("segundo angulo do triangulo "))
c = float(input("terceiro angulo do triangulo "))
#apenas valores positivos aceitos 
if a < 0 or b < 0 or c < 0:
    print("apenas valores positivos são aceitos")
else:
    #o resultado da soma deve ser 180
    if a+b+c != 180:
        print("esses angulos não formam um triangulo")
    elif a > 90 or b > 90 or c > 90:
        print("esse é um triangulo obtuso")
    elif a == 90 or b == 90 or c == 90:
        print("esse é um triangulo reto")
    else:
        print("esse é um triangulo agudo")