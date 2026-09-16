"""Construa uma função que receba uma data no formato DD/MM/AAAA (string) e
devolva uma string com a data por extenso, por exemplo: “doze de agosto de dois mil e
vinte e quatro”. Seu algoritmo deve ser capaz de converter datas entre os anos de 2000 e
2100."""

def numero(n):
    unidades=["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove"]
    especiais=["dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove"]
    dezenas=["","","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]
    if n<10:
        return unidades[n]
    elif n<20:
        return especiais[n-10]
    elif n<100:
        d=n//10
        u=n%10
        if u==0:
            return dezenas[d]
        else:
            return dezenas[d]+" e "+unidades[u]
def ano_extenso(ano):
    if ano==2000:
        return "dois mil"
    resto=ano-2000
    if resto<100:
        return "dois mil e "+numero(resto)
    else:
        return "dois mil e "+numero(resto)
def data_extenso(data):
    meses=["janeiro","fevereiro","março","abril","maio","junho",
           "julho","agosto","setembro","outubro","novembro","dezembro"]
    partes=data.split("/")
    dia=int(partes[0])
    mes=int(partes[1])
    ano=int(partes[2])
    return numero(dia)+" de "+meses[mes-1]+" de "+ano_extenso(ano)

data=input("digite uma data no formato DD/MM/AAAA:")
print(data_extenso(data))