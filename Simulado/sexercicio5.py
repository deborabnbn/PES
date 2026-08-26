# 5 – Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:
# • 1 – Adição;
# • 2 – Subtração;
# • 3 – Multiplicação;
# • 4 – Divisão;
# • 0 – Sair.
# Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
# mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.


contador = -1
while contador != 0:
    print("""
        1 – Adição
        2 – Subtração
        3 – Multiplicação
        4 – Divisão
        0 – Sair
    """)

    num1 = float(input("digite um número: "))
    num2 = float(input("digite o segundo número: "))
    opcao = int(input("digite uma  opção: "))
    
    if opcao == 1:
        soma = (num1 + num2)
        print(soma)

    elif opcao == 2:
        subitracao = (num1 - num2)
        print(subitracao)

    elif opcao == 3:
        multiplicacao = (num1 * num2)
        print(multiplicacao)

    elif opcao == 4:
        divisao = (num1 / num2)
        print(divisao)
    
    else:
        print ("opção invalida")
    
