aux = 0
auxm = 0
auxh = 0
somat = 0
somam = 0
somah = 0
while aux <=5:
    i = int(input("informe a idade: "))
    s = input("selecioe o sexo M(Mulher) H(Homem)")
    if s == "m":
        somat = somat+i
        somam = somam +i
        auxm +=1
    elif s == "h":
        somat = somat+i
        somah = somah+i
        auxh +=1  
    aux +=1
print(f"a média das idades é {somat/5} a média das idades femininas {somam/auxm} a média das idades masculina {somah/auxh}")