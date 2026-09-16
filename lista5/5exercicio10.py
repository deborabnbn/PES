"""Construa uma função que receba uma string como parâmetro e devolva (retorne)
outra string com os caracteres embaralhados. Por exemplo: se função receber a palavra
python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma
aleatória. Padronize sua função que todos os caracteres sejam devolvidos em caixa alta
ou caixa baixa, independentemente de como foram digitados. Para lhe auxiliar nesse
exercício, pesquisa sobre a biblioteca Random do Python."""

import random
def embaralhar(palavra):
    maiusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M",
                "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    minusculas=["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    nova=""
    for letra in palavra:
        for i in range(0,26):
            if letra==maiusculas[i]:
                nova=nova+minusculas[i]
            if letra==minusculas[i]:
                nova=nova+minusculas[i]
    lista=list(nova)
    random.shuffle(lista)
    nova=""
    for i in lista:
        nova=nova+i
    return nova
p=input("digite uma palavra:")
print(embaralhar(p))