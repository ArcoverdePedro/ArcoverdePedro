palavra = input("digite uma palavra: ")
aux = 1
aux1 = 1
aux2 = len(palavra)-1
while aux1 <= (len(palavra)*2):
    if aux <= len(palavra):
        print(palavra[:aux])
        aux+=1
    elif aux > len(palavra):
        print(palavra[:aux2])
        aux2-=1
    aux1+=1