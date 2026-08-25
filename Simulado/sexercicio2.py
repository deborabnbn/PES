# 2 – Elabore um algoritmo que leia 15 números de uma cartela de bingo e armazene-os em uma lista.
# Aceite apenas números entre 1 e 75 e não permita valores repetidos. Ao final, ordene a lista e
# exiba os números do menor para o maior.

lista = []
contador = 0
while contador < 15:
    num = int(input("Digite número: "))
    if num >=1 and num<=75:
        if num in lista:
            print("Este número ja está na lista")
        else:
            lista.append(num)
    else:
        print ("esse número não é aceito")
    contador = contador +1 
lista.sort()
print (lista)

    


