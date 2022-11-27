x = int(input("defina  ponto x: "))
y = int(input("defina  ponto y: "))
if x > 0 and y > 0 :
    print(f"o ponto{x,y} está no primeiro quadrante")
elif x < 0 and y < 0:
    print(f"o ponto{x,y} está no terceiro quadrante")
elif x < 0 and y > 0:
    print(f"o ponto{x,y} está no quarto quadrante")
elif x > 0 and y < 0:
    print(f"o ponto{x,y} está no segundo quadrante")
else:
    print("o ponto é nulo, ou seja, x e y é zero")