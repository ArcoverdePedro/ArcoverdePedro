x = int(input("informe um an entre 1900 e 2100: "))
if x < 1900 or x > 2100:
    print("O valor informado não faz parte do periodo determinado. ")
#o ano bissexto apenas é divisivel, com resto 0, por 4
elif x % 4 == 0:
    print("esse é um ano bissexto")
else:
    print("Esse ano não é bissexto")