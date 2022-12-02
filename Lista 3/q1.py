dec = int(input("informe um valor para transforma-lo em binario: "))
binario = ""
while dec >0:
    resto = dec%2
    dec = dec //2
    binario = str(resto)+binario
print(binario)