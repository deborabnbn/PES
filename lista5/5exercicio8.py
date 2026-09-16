# 8 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada no formato
# de string, por exemplo: “15:31”. Deve haver pelo menos duas funções: uma para fazer a
# conversão e uma para imprimir a saída. A função que faz a conversão deve ter duas
# saídas: uma com a hora convertida e outra com “A”, caso seja “A.M.” e “P”, caso seja
# “P.M.”. Inclua um loop que permita que o usuário repita esse cálculo para novos valores
# de entrada todas as vezes que desejar.


def separar(horas):
   lh = horas.split(":")
   return lh
def horario(hora):
   if hora<=11:
       am=True
   else:
       am=False
   return am
while True:
   h=(input("Digite a hora (HH:MM) ou digite 0 para sair:"))
   if h!="0":
       lista=separar(h)
       ho=int(lista[0])
       mi=lista[1]
       ho2=horario(ho)
       if ho2==True:
           print(f'{ho}:{mi} A.M')
       else:
           ho=ho-12
           print(f'{ho}:{mi} P.M')
   else:
       exit(0)