palavra_chave = 'CABIDE'
aux = palavra_chave
qnt = len(palavra_chave)
acertos = 0
qnterros = 6
tentativas = ''
while True:
    letra = str(input('coloque uma letra: ')).upper()
    cont = tentativas.find(letra)
    forca = palavra_chave.find(letra)
    if cont != -1:
        print(f'{letra} Letra ja informada')
    elif forca != -1:
        palavra_chave = palavra_chave.replace(letra,'')
        qnt = len(palavra_chave)
        print(f'{letra} está presente, faltam {qnt}')
        acertos += 1
    else:
        print(f'{letra} não está presente, você tem {qnterros-1} erro(s).')
        qnterros -= 1
    tentativas += letra
    if qnterros == 0 or qnt == 0:
         break
if qnt == 0:
    print(f'Você ganhou, a palavra era: {aux}')
elif qnterros == 0:
    print(f'Você perdeu')