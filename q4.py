x = int(input("qual o valor ? "))
if x == 0:
    print("valor nulo")
elif x > 0 and x % 2 == 0:
    print("valor par e positivo")
elif x < 0 and x % 2 == 0:
    print("valor par e negativo")
elif x < 0 and x % 2 != 0:
    print("valor impar e negativo")
else:
    print("valor impar e positivo")
