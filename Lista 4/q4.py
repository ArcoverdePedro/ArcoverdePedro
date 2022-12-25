#sem usar while
'''
nm1 = input("coloque um nome ou um numero ")
nm2 = nm1[::-1]
nmaux1 = nm1.replace(" ", "")
nmaux2 = nm2.replace(" ", "")
if nmaux1.upper() == nmaux2.upper():
    print (f"{nm1}, {nm2} São palindromos")
else: print ('não é um palindromo')'''

#usando while
palavra = input('digite uma palavra: ')
palavra1 = palavra.replace(' ', '').upper()
pos = len(palavra1)-1
aux = 0
while pos > aux and palavra1[aux] == palavra1[pos]:
    pos -= 1
    aux += 1
if palavra1[aux] == palavra1[pos]: print(f"> {palavra} < é um Palíndromo!")
else:
     print(f"{palavra} não é um Palíndromo! ")
