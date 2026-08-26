# 3 – Faça um algoritmo que leia o preço de um produto e a quantidade comprada. Calcule o total
# da compra e, caso ele seja maior ou igual a R$ 100,00, aplique um desconto de 10%. Ao final,
# exiba o valor a ser pago. 

produto_preco = float(input("digite o preço do produto: "))
produto_quant = int(input("digite a quantidade do produto: "))
total_compra = produto_preco * produto_quant
if total_compra >= 100:
    total_compra = total_compra * 1.10
    print ("sua compra ficou",total_compra)
else:
    print ("sua compra ficou", total_compra)