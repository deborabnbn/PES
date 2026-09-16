prof={'001' : "Prof Thiago Paes",
'002' : "Prof Schalata",
'003' : "Prof Ignácio",
'004' : "Prof Ryan",
'005' : "Prof André",
'006' : "Profª Fabiana",
'007' : "Prof Alberto",
'008': "Prof Juliano",
'009' : "Prof Thiago Waltrik",
'010': "Prof João Eduardo"}

lab102 = ['003', '001', '004', '005', '006']
lab103 = ['007']
lab104 = ['004', '008', '002','005']
lab105 = ['003','007','009', '001']
lab106 = ['002', '003', '009', '001']
lab107 = ['005', '002', '009', '001', '010']

while True:
    x=int(input("para professores: 1 – Cadastrar, 2 - Excluir, 3 - Listar, 4-entrar em labs, 5-alterar; digite a opçaõ escolhida:"))
    if x==1:
        cod=(input("qual o codigo do professor?"))
        if cod in prof:
            print ("esse codigo ja esta sendo usado")
        else:
            nome=(input("qual o nome do professor?"))
            prof [cod]=nome
            print ("sucesso!")
    else:
        if x==2:
            r=input("qual o codigo do professor voce quer remover?")
            if r in prof:
                if r in lab102 or r in lab103 or r in lab104 or r in lab105 or r in lab106 or r in lab107:
                    print ("esse professor tem acesso ao labs, para excliu-lo exclua primeiro os acesso que ele tem")
                else:
                    del prof [r]
                    print ("sucesso!")
            else:
                print ("esse codigo nao existe")
        else:
            if x==3:
                if len(prof)==0:
                    print ("nao ha professores")
                else:
                    for cod, nome in prof.items():
                        print (f'{cod}-{nome}')
            else:
                if x==5:
                    r=input("qual o codigo do professor voce quer alterar?")
                    if r in prof:
                        if r in lab102 or r in lab103 or r in lab104 or r in lab105 or r in lab106 or r in lab107:
                            print ("esse professor tem acesso ao labs, para altera-lo exclua primeiro os acesso que ele tem")
                        else:
                            n=input("qual nome voce quer por no codigo")
                            for cod, nome in prof.items():
                                nome=n
                                print ("sucesso!")
                    else:
                        print ("esse codigo nao existe")
                else:
                    if x==4:
                        while True:
                            x=int(input("para professores em laboratórios: 1 – Cadastrar, 2 - Excluir, 3 - Listar, 4-procurar nos labs, 0 - Sair ; digite a opçaõ escolhida:"))
                            if x==1:
                                lab=(input("qual o lab que voce quer por o professor?"))
                                cod=(input("qual o professor que voce quer por no lab?"))
                                if lab == "lab102":                           
                                    if cod in lab102:
                                        print ("esse codigo ja esta sendo usado")
                                    else:
                                        lab102.append(cod) 
                                        print ("sucesso!")
                                else:
                                    if lab == "lab103":
                                        if cod in lab103:
                                            print ("esse codigo ja esta sendo usado")
                                        else:
                                            lab103.append(cod) 
                                            print ("sucesso!")
                                    else:
                                        if lab == "lab104":
                                            if cod in lab104:
                                                print ("esse codigo ja esta sendo usado")
                                            else:
                                                lab104.append(cod) 
                                                print ("sucesso!")
                                        else:
                                            if lab == "lab105":                           
                                                if cod in lab105:
                                                    print ("esse codigo ja esta sendo usado")
                                                else:
                                                    lab105.append(cod) 
                                                    print ("sucesso!")
                                            else:
                                                if lab == "lab106":
                                                    if cod in lab106:
                                                        print ("esse codigo ja esta sendo usado")
                                                    else:
                                                        lab106.append(cod) 
                                                        print ("sucesso!")
                                                else:
                                                    if lab == "lab107":
                                                        if cod in lab107:
                                                            print ("esse codigo ja esta sendo usado")
                                                        else:
                                                            lab107.append(cod) 
                                                            print ("sucesso!")
                            else:
                                if x==2:
                                    r=input("qual o codigo do professor voce quer remover?")
                                    lab=(input("qual o lab que voce quer remover o professor?"))
                                    if lab == "lab102":                           
                                        if r in lab102:
                                            lab102.remove(r)
                                            print ("sucesso!")
                                        else:
                                            print ("esse professor nao esta nesse lab")
                                    else:
                                        if lab == "lab103":
                                            if r in lab103:
                                                lab103.remove(r)
                                                print ("sucesso!")
                                            else:
                                                print ("esse professor nao esta nesse lab")
                                        else:
                                            if lab == "lab104":
                                                if r in lab104:
                                                    lab104.remove(r)
                                                    print ("sucesso!")
                                                else:
                                                    print ("esse professor nao esta nesse lab")
                                            else:
                                                if lab == "lab105":                           
                                                    if r in lab105:
                                                        lab105.remove(r)
                                                        print ("sucesso!")
                                                    else:
                                                        print ("esse professor nao esta nesse lab")
                                                else:
                                                    if lab == "lab106":
                                                        if r in lab106:
                                                            lab106.remove(r)
                                                            print ("sucesso!")
                                                        else:
                                                            print ("esse professor nao esta nesse lab")
                                                    else:
                                                        if lab == "lab107":
                                                            if r in lab107:
                                                                lab107.remove(r)
                                                                print ("sucesso!")
                                                            else:
                                                                print ("esse professor nao esta nesse lab")
                                else:
                                    if x==3:
                                        print ("lab102:", lab102, "\n" "lab103:",lab103,"\n""lab104:",lab104,"\n""lab105:", lab105,"\n""lab106:", lab106,"\n""lab107:", lab107) 
                                    else:
                                        if x==4:
                                            lab=input("em qual lab voce quer procurar?")
                                            cod=input("qual o cod do professor que voce quer procurar?")
                                            if lab== "lab102":
                                                if cod in lab102:
                                                    print("professor", cod, "esta no lab102")
                                                else:
                                                    print("esse professore nao esta nesse lab")
                                            else:
                                                if lab== "lab103":
                                                    if cod in lab103:
                                                        print("professor", cod, "esta no lab103")
                                                    else:
                                                        print("esse professore nao esta nesse lab")
                                                else:
                                                    if lab== "lab104":
                                                        if cod in lab104:
                                                            print("professor", cod, "esta no lab104")
                                                        else:
                                                            print("esse professore nao esta nesse lab")
                                                    else:
                                                        if lab== "lab105":
                                                            if cod in lab105:
                                                                print("professor", cod, "esta no lab105")
                                                            else:
                                                                print("esse professore nao esta nesse lab")
                                                        else:   
                                                            if lab== "lab106":
                                                                if cod in lab106:
                                                                    print("professor", cod, "esta no lab106")
                                                                else:
                                                                    print("esse professore nao esta nesse lab")
                                                            else:  
                                                                if lab== "lab107":
                                                                    if cod in lab107:
                                                                        print("professor", cod, "esta no lab107")
                                                                    else:
                                                                        print("esse professore nao esta nesse lab")  
                                        else:
                                            if x==0:
                                                break