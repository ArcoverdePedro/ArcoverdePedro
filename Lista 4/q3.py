frs = input("digite uma frase a seguir: ")
plva = input("digite uma palavra, do texto, a ser substituida:")
plvn = input("digite uma nova palavra para substituir: ")
#substituir palavra antiga pela nova na frase
frs = frs.replace(plva, plvn)
print (frs)