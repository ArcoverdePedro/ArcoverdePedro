a = 1
somador = 0
while a != 0:
    a=int(input("digite um numero: "))
    somador = somador+a
    if a == 0:
        print(f"a soma de todos os valores é {somador}")