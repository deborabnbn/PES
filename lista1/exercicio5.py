temperatura = float(input("Digite temperatura: "))
if temperatura < 10:
    print("Está muito frio! Use roupas quentes.")
elif 10 <= temperatura <= 20:
    print("Frio. Vista-se bem")
elif 20 < temperatura <= 25:
    print("Temperatura agradável")
elif 25 < temperatura <= 30:
    print("Está ficando quente!")
elif temperatura > 30:
    print("Está muito quente! Fique hidratado")