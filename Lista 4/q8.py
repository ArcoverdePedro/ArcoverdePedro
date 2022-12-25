cpf = input("digite os numeros de um cpf: ")
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
    print("cpf inválido")