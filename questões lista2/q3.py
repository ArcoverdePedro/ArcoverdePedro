x = int(input("qual o valor do cateto adjacente? "))
y = int(input("qual o valor do cateto oposto? "))
#condicional, apenas positivos aceitos
if x < 0 or y < 0:
    print("apenas valores positivos são aceitos")
else:
    print(f"o valor da hipotenusa é {(x**2+y**2)**(1/2)}")