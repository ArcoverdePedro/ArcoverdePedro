pi = (float(input("determine o peso inicial em gramas: ")))
pf = pi
aux = 0
tmph = 0
tmpm = 0
tmps = 0
#calculando a meia vida no laço seguinte
while pf >= 0.5:
    pf = pf/2
    aux +=1
tmph = (aux * 50)/3600
tmpm = (aux * 50)/60
tmps = aux*50
tmpt = (aux*50)//3600,((aux*50)%3600)//60,(aux*50)%60
print(type (tmpt))
print(f"massa inicial: {pi} Massa final: {pf} Tempo em horas: {tmph} Tempo em Minutos: {tmpm} Tempo em Segundos {tmps} e o tempo em hora,minuto e segundo {tmpt}")