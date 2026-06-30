# 1 Suco R$ 6,00
# 2 Pão de queijo R$ 3,00
# 3 Pastel R$ 7,00
# 4 Salada de frutas R$ 9,00
# 5 Café com leite R$ 3,50
# 6 Cappuccino R$ 4,50
# 7 Iogurte R$ 6,50
# 8 Água R$ 2,50
caixa = 0 
codigo = 20

while codigo != 0:
    codigo = int(input("digite codigo: "))
    quantidade = int(input("digite quantidade comprada: "))
    if codigo == 1:
        total = quantidade*6
        print("suco",total)

    elif codigo == 2:
        total = quantidade*3
        print("pão de queijo",total)

    elif codigo == 3:
        total = quantidade*7
        print("pastel",total)

    elif codigo == 4:
        total = quantidade*9
        print("salada de frutas", total)

    elif codigo == 5:
        total = quantidade*3.50
        print("café com leite", total)

    elif codigo == 6:
        total = quantidade*4.50
        print("cappuccino",total)

    elif codigo == 7:
        total = quantidade*6.50
        print("iorgute", total)

    elif codigo == 8:
        total = quantidade*2.50
        print("agua", total)
    caixa = caixa + total
    total = 0
    
print("quantidade no caixa em reais:",caixa)