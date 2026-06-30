
# – Implemente um programa para calcular sua média final em uma determinada unidade
# curricular. O programa deve solicitar ao usuário a quantidade de notas, o valor para cada
# uma das notas e exibir, ao final, a média aritmética simples e informar se o(a) estudante
# está Aprovado ou Reprovado. Considere que a média mínima para a aprovação é 6.

quantNOTAS = int(input("digite a quantidade de notas: "))
n = 1
while n <= quantNOTAS:
    print (n)
    n = n + 1
m = 1
total = 0
while m < n:
    #total = total + int(input("digite a nota: "))
    total += int(input("digite a nota: "))
    m = m + 1
media = total/n
if media < 6:
    print ("reprovado")
else:
    print ("aprovado!")