lst_uf        = ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']
lst_siglas    = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
lst_populacao = [3365351, 14985284, 9240580, 7153262, 4059905, 9674793, 3289290, 3560903, 2338474]

# O programa deve solicitar a sigla da uf e excluir as informações
# caso a sigla informada exista na lista, lembrar de excluir das 
# demais listas.
while True:
    sigla = input("informe a sigla que você deseja saber:").upper()
    if sigla in lst_siglas:
        pos = lst_siglas.index(sigla)
        lst_uf.pop(pos) 
        lst_siglas.pop(pos) 
        lst_populacao.pop(pos)
        print(f"listas: nomes:{lst_uf}\nSiglas:{lst_siglas}\nPopulação:{lst_populacao}")
        break
    else:
        print(f"informe a sigla certa vagabundo!!!\n{lst_uf}\n{lst_siglas}\n{lst_populacao}")