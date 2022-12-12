vlr = int(input("digite um valor ou 0 para parar: "))
vlrmenor = vlr
vlrmaior = vlr
soma = vlr
somador = 0
while vlr != 0:
    vlr = int(input("digite um valor ou 0 para parar: "))#substituição do menor valor
    if vlrmenor >= vlr and vlr != 0:
        vlrmenor = vlr#substituição do maior valor
    if vlrmaior <= vlr:
        vlrmaior = vlr
    soma = soma + vlr
    somador +=1
print((f"o maior valor é {vlrmaior}, o maior valor é: {vlrmenor}, a média é: {soma/somador}"))