# 5 – Programe um algoritmo com mais algumas funções úteis para a manipulação de listas
# numéricas:
# As funções dos itens b, c e d devem retornar -1 caso a lista esteja vazia. No seu
# programa principal, crie duas listas (uma vazia e outra com alguns elementos) e teste
# (comprove) o funcionamento de cada uma das funções.

# a) uma função que receba uma lista e retorne True, caso esteja vazia, ou False, caso
# possua um ou mais elementos;
def true_or_false(lista):
    if len(lista) == 0:
        return True
    else:
        return False
    
lista = []
resultado = true_or_false(lista)
if resultado:
    print("Esta vazia")
else:
    print("Esta cheia")

# b) uma função que receba uma lista e retorne o maior valor;
def maior_valor(lista):
    if len(lista) == 0:
        return -1
    indice = 0
    maior_vl = lista[0]

    while indice < len(lista):
        if lista[indice] > maior_vl:
            maior_vl = lista[indice]
        indice = indice + 1
    return maior_vl

lista = [1, 2, 3, 6, 4]
resultado = maior_valor(lista)
print(resultado)

# c) uma função que receba uma lista e retorne o menor valor;
def menor_valor(lista):
    if len(lista) == 0:
        return -1
    
    indice = 0
    menor_vl = lista[0]
    while indice < len(lista):
        if lista[indice] < menor_vl:
            menor_vl = lista[indice]
        indice = indice +1
    return menor_vl
lista = [1, 2 ,3, 6, 4]
resultado = menor_valor(lista)
print(resultado)

# d) uma função que receba uma lista e retorne o valor médio.
def valor_medio(lista):
    if len(lista) == 0:
        return -1
    
    indice = 0 
    soma = 0
    quant_total = 0
    while indice < len(lista):
        soma += lista[indice]
        quant_total = quant_total+1
        indice = indice +1
    media = soma/quant_total 
    return media

lista = [7, 8, 9]
resultado = valor_medio(lista)
print(resultado)

lista_vazia = []
lista_elementos = [1, 2, 3, 6, 4]

print("LISTA VAZIA")
print(true_or_false(lista_vazia))
print(maior_valor(lista_vazia))
print(menor_valor(lista_vazia))
print(valor_medio(lista_vazia))

print("\nLISTA COM ELEMENTOS")
print(true_or_false(lista_elementos))
print(maior_valor(lista_elementos))
print(menor_valor(lista_elementos))
print(valor_medio(lista_elementos))
