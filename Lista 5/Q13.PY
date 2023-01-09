DEFAULT_PASSWORD = 'swordfish'
password = input('informe a senha: ')
for counter in range(1000000):
    if password == DEFAULT_PASSWORD:
        print('Senha correta! Bem vindo!:')
        break
    else: password = input('Senha incorreta. Tente novamente: ')