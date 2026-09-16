"""Crie um algoritmo com uma função que retorna um valor em reais escrito por
extenso. Por exemplo, caso seja passado “1.74” como parâmetro para a função, ela deve
retornar: um real e setenta e quatro centavos. Caso seja passado “3251.90”, deve retornar
“três mil duzentos e cinquenta e um reais e noventa centavos”."""
def numero(n):
    unidades=["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove"]
    especiais=["dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove"]
    dezenas=["","","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]
    centenas=["","cento","duzentos","trezentos","quatrocentos","quinhentos",
              "seiscentos","setecentos","oitocentos","novecentos"]
    if n==0:
        return "zero"
    if n<10:
        return unidades[n]
    if n<20:
        return especiais[n-10]
    if n<100:
        d=n//10
        u=n%10
        if u==0:
            return dezenas[d]
        else:
            return dezenas[d]+" e "+unidades[u]
    if n==100:
        return "cem"
    c=n//100
    resto=n%100
    if resto==0:
        return centenas[c]
    return centenas[c]+" e "+numero(resto)

def dinheiro(valor):
    partes=valor.split(".")
    reais=int(partes[0])
    centavos=int(partes[1])
    milhares=reais//1000
    resto=reais%1000
    texto=""
    if milhares>0:
        if milhares==1:
            texto="mil"
        else:
            texto=numero(milhares)+" mil"
    if resto>0:
        if texto!="":
            texto=texto+" "+numero(resto)
        else:
            texto=numero(resto)
    if reais==1:
        texto=texto+" real"
    else:
        texto=texto+" reais"
    if centavos==1:
        texto=texto+" e um centavo"
    elif centavos>0:
        texto=texto+" e "+numero(centavos)+" centavos"
    return texto
valor=input("digite um valor:")
print(dinheiro(valor))