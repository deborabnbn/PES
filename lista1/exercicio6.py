jogador1 = input ("digite escolha1:  ")
jogador2 = input ("digite escolha2: ")
if jogador1 == "tesoura" and jogador2 == "papel": 
    print ("jogador1 venceu!")
elif jogador1 == "tesoura" and jogador2 == "tesoura":
    print ("empate!")
elif jogador1 == "pedra" and jogador2 == "pedra":
    print ("empate!")
elif jogador1 == "papel" and jogador2 == "papel":
    print ("empate!")    
elif jogador1 == "papel" and jogador2 == "tesoura":
    print ("jogador2 venceu!")
elif jogador1 == "pedra" and jogador2 == "tesoura":
    print ("jogador1 venceu!")
elif jogador1 == "tesoura" and jogador2 == "pedra":
    print ("jogador2 venceu!")
elif jogador1 == "papel" and jogador2 == "pedra":
    print ("jogador1 venceu!")
elif jogador1 == "pedra" and jogador2 == "papel":
    print ("jogador2 venceu!")
