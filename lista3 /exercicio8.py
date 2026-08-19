#8 – Suponha que você recebeu a última fatura do seu cartão de crédito no valor de R$
#1.000,00 e que você não possa pagá-la. Faça um programa que calcule sua dívida total
#com o banco depois de uma quantidade de meses informada durante a execução do 
#programa. Considere que a taxa de juros mensal de um cartão de crédito é de 15,30% ao
#mês. Fonte da taxa de juros utilizada: https://einvestidor.estadao.com.br/educacaofinanceira/juros-cartao-de-credito-dicas-para-evitar-dividas/
#A título de curiosidade, simule sua dívida final no prazo de 2 anos (24 meses).

quantMESES = int(input("digite a quantidade de meses: "))
valorDIVIDA = float(input("digite o valor da divida: "))
totalJUROS = quantMESES*(0.153*valorDIVIDA)
totalDIVIDA = totalJUROS + valorDIVIDA
print (totalDIVIDA)