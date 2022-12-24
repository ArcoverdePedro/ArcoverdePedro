palavra = input("digite uma palavra: ")
aux = 0
#imprimindo letra por letra
while aux < len(palavra)+1:
    print(palavra[0:aux])
    aux +=1