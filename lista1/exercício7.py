dia = int(input("escreva dia: "))
mes = input("escreva mes: ").lower()

if (mes == "janeiro" and dia >= 21 and dia <= 31) or (mes == "fevereiro" and dia <= 18):
    print("seu signo é Aquário")

elif (mes == "fevereiro" and dia >= 19 and dia <= 29) or (mes == "março" and dia <= 20):
    print("seu signo é Peixes")

elif (mes == "março" and dia >= 21 and dia <= 31) or (mes == "abril" and dia <= 20):
    print("seu signo é Áries")

elif (mes == "abril" and dia >= 21 and dia <= 30) or (mes == "maio" and dia <= 20):
    print("seu signo é Touro")

elif (mes == "maio" and dia >= 21 and dia <= 31) or (mes == "junho" and dia <= 20):
    print("seu signo é Gêmeos")

elif (mes == "junho" and dia >= 21 and dia <= 30) or (mes == "julho" and dia <= 22):
    print("seu signo é Câncer")

elif (mes == "julho" and dia >= 23 and dia <= 31) or (mes == "agosto" and dia <= 22):
    print("seu signo é Leão")

elif (mes == "agosto" and dia >= 23 and dia <= 31) or (mes == "setembro" and dia <= 22):
    print("seu signo é Virgem")

elif (mes == "setembro" and dia >= 23 and dia <= 30) or (mes == "outubro" and dia <= 22):
    print("seu signo é Libra")

elif (mes == "outubro" and dia >= 23 and dia <= 31) or (mes == "novembro" and dia <= 21):
    print("seu signo é Escorpião")

elif (mes == "novembro" and dia >= 22 and dia <= 30) or (mes == "dezembro" and dia <= 21):
    print("seu signo é Sagitário")

elif (mes == "dezembro" and dia >= 22 and dia <= 31) or (mes == "janeiro" and dia <= 20):
    print("seu signo é Capricórnio")

else:
    print("Data inválida.")