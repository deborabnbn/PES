# Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como chaves e seus
# significados como valores. Inicie com:
# "apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma
# situação difícil, ou usar de meios extremos e exagerados"
# Solicite ao usuário mais 4 palavras e seus respectivos significados. Em seguida, peça uma
# palavra para consulta e exiba seu significado. Caso ela não esteja cadastrada, informe “Palavra
# não encontrada”.




dicionario = {
    "apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados"
}

contador = 0

while contador < 4:
    palavra = input("Digite uma palavra: ")
    significado = input("Digite o significado: ")

    dicionario[palavra] = significado

    contador = contador +1

palavra_consulta = input("Digite uma palavra para consultar: ")

if palavra_consulta in dicionario:
    print(dicionario[palavra_consulta])
else:
    print("Palavra não encontrada")
