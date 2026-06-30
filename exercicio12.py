operacao = 10000
while operacao != 0:
    num1 = float(input("digite numero: "))
    num2 = float(input("digite numero: "))
    operacao = input("digite operacao: ")
    if operacao == "soma":
        print (num1+num2)
    elif operacao == "divisao":
        print (num1/num2)
    elif operacao == "subtracao":
        print (num1/num2)
    elif operacao == "multiplicacao":
        print (num1*num2)
