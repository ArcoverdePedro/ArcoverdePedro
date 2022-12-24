peso = float(input("qual o seu peso? "))
altura = float(input("qual a sua altura em cm? "))
imc = peso/altura**2
if imc < 18.5:
    print(f"seu imc é {imc}, você está abaixo do peso")
elif imc < 24.9:
    print(f"seu imc é {imc}, você está em um peso adequado")
elif imc < 29.9:
    print(f"seu imc é {imc}, você está sobrepeso")
elif imc < 34.9:
    print(f"seu imc é {imc}, você está no grau 1 de obesidade")
elif imc < 39.9:
    print(f"seu imc é {imc}, você está no grau 2 de obesidade")
else:
    print(f"seu imc é {imc}, você está no grau 3 de obesidade ")