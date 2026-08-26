# 8 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada no formato
# de string, por exemplo: “15:31”. Deve haver pelo menos duas funções: uma para fazer a
# conversão e uma para imprimir a saída. A função que faz a conversão deve ter duas
# saídas: uma com a hora convertida e outra com “A”, caso seja “A.M.” e “P”, caso seja
# “P.M.”. Inclua um loop que permita que o usuário repita esse cálculo para novos valores
# de entrada todas as vezes que desejar.

def converter_hora(hora):
    hora = int(hora)

    if hora > 12:
       hora = hora -12
       hora = "PM " + str(hora)
    else:
       hora = "AM " + str(hora)
    
    return hora

def converter_hora_minuto(hora_minuto): # "13:04"
   hora = hora_minuto.split(":")[0] # "13"
   minuto = hora_minuto.split(":")[1] # "04"
   
   hora = converter_hora(hora) 

   return hora + ":" + minuto


contador = 0
while contador != -1:
    
    


def converter():

 hora = float(input("digite o horário: "))
 if hora > 12.00:
 