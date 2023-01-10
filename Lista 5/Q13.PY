DEFAULT_PASSWORD = 'swordfish'
psswrd = input(f"informe a senha")
while psswrd != DEFAULT_PASSWORD:
    print(f"{psswrd} não é a senha correta")
    psswrd = input("informe a senha")
if psswrd == DEFAULT_PASSWORD:
    print(f"senha correta") 