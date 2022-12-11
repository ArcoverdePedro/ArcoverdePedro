valor = float(input('O valor inicial de sua aplicação:'))
tx = float(input('O ganho será feito em uma taxa de:'))
rend = 0
qtd_mes = 1
um_ano = 12
if valor and tx != 0:
    while qtd_mes <= um_ano:
        qtd_mes +=1
        tx = (1+tx/100)
        rend_m = valor *tx #rendimento mensal é o valor investido * a taxa
        rend = valor + rend_m ** um_ano #o redndimento total é o valor mais o rendimento mensal, elevado ao tempo de aplicação (até parar)
        if qtd_mes == um_ano: break
        a = str (input('Deseja calcular mais um um_ano?'))
        if a == 's': continue
        elif a == 'n':break
    print(rend)