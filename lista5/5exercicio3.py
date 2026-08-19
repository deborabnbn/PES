# 3 – Codifique um programa com uma função para calcular o volume de um cilindro. Seu
# programa principal deve solicitar a altura e o raio do cilindro em metros, chamar a função
# e exibir o resultado na tela. 

def volume_cilindro(h, r):
    volume = h*3*r**2
    print(volume)
              
altura = float(input("Digite a aluta do cilindro"))
raio = float(input("digite o raio do cilindro"))

volume_cilindro(altura, raio)