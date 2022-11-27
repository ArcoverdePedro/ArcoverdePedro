x = int(input("qual o valor ? "))
if x == 0:
    print("valor nulo")
elif x > 0 and x % 2 == 0:
    print("valor {x} par e positivo")
elif x < 0 and x % 2 == 0:
    print("valor {x} par e negativo")
elif x < 0 and x % 2 != 0:
    print("valor {x} impar e negativo")
else:
    print("valor {x} impar e positivo")
