caminhao={
'001' :"Monobloco",
'002' : "Scania 112 HW",
'003' : "Volkswagen Express 4150",
'004' : "Volkswagen Express 6160",
'005' : "Volkswagen VW 17230 Worker",
'006' : "Volkswagen Express 9170",
'007' : "Iveco Daily 40s14",
'008' : "Iveco Tectro 310E28"}

condutor={
'001' : "Roberto Souza",
'002' : "João Graciano",
'003' : "Karine Silva",
'004' : "Pedro Luiz",
'005' : "Maria Catarina",
'006' : "Júlio Cardoso",
'007' : "Altivo Antônio",
'008' : "Jorge Gonçalves",
'009' : "Marcos Vinícius",
'010' : "Heleno Nunes",
'011' : "Mara Cristina",
'012' : "Otávio Rocha"}

registros = []

while True:
    x=int(input("1-listar caminhoes, 2-listar condutores, 3-registro de saida, 4-registro de chegada, 5-entregas do dia:"))
    if x==1:
        for cod, nome in caminhao.items():
            print (f'{cod}-{nome}')
    else:
        if x==2:
            for cod, nome in condutor.items():
                print (f'{cod}-{nome}')
        else:
            if x==3:
                codcami = int(input("qual o codigo do caminhao que esta saindo?"))
                for i in registros:
                    if codcami==i["cod_caminhao"]:
                        cont=1
                if cont==1:
                    print("esse caminhao nao esta disponivel.")  
                else:
                    codcond = int(input("qual o codigo do condutor que esta saindo com o caminhao informado anteriormente?"))
                    datasaída = (input("qual o data de saida (dd/mm/aaaa)?"))
                    horasaída = (input("qual a hora de saida (hh:mm)?"))
                    registro = { 
                        "cod_caminhao" : codcami,
                        "cod_condutor" : codcond,
                        "data_saida" : datasaída,
                        "hora_saida" : horasaída,
                        "data_chegada" : '',
                        "hora_chegada" : '' }
                    registros.append(registro)
                    print ("sucesso!")
            else:
                if x==4:
                    codi = int(input("qual o cod do caminhao que chegou?"))
                    esta = False
                    for r in registros:
                        if r["cod_caminhao"] == codi:
                            datacheg = (input("qual a data que o caminhao chegou (dd/mm/aaaa)?"))
                            horacheg = (input("qual a hora que o caminhao chegou (hh:mm)?"))
                            r["data_chegada"] = datacheg
                            r["hora_chegada"] = horacheg
                            print ("sucesso!")
                            esta = True
                            break
                    if esta == False:
                        print("Esse caminhão não saiu =)")
                else:
                    if x==5:
                        cont=0
                        for r in registros:
                            if r["data_chegada"] == '':
                                cont= cont+1
                        if cont==0:
                            print("todas as entregas ja foram concluida.")
                        else:
                            print ("faltam", cont, "entregas")