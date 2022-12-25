#modelo ineficiente
'''cpf = input("digite os numeros de um cpf: ")
aux = 0
somador = 0
if len(cpf) == 11:
    while aux < len(cpf): 
        #enquanto o auxiliar é menor que a quantidade de numeros do cpf o codigo roda
        somador = somador + int(cpf[aux]) 
        #a soma de todos os numeros de um cpf devem ser dois numero iguais ex. 44, 55, 66
        strsoma = str(somador)
        aux += 1
    if strsoma[0] == strsoma[1]: 
        #comparação se os valores batem
        print(f"seu CPF {cpf} é valido")    
else:
    print("cpf inválido")'''
#funciona em 100% dos casos
cpf = input('digite um cpf para verificar: ')
somar = 0
aux = 1
cont= 0
if len(cpf) == 11:
    #verificando o primeiro digito
    while cont <=8:
        somar = somar + int(cpf[cont]) * aux
        aux +=1
        cont+=1
    if somar%11 == int(cpf[9]) or somar%11 == 10 and int(cpf[9]) == 0:
        aux = 0
        cont = 0
        somar = 0
        while cont <=9:
            somar = somar + int(cpf[cont]) * aux
            aux+=1
            cont+=1
        if somar%11 == int(cpf[10]) or somar%11 == 10 and int(cpf[10]) == 0:
            print(f"Cpf {cpf}, Válido")