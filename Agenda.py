import time

dias = {1:"disponível",2:"disponível",3:"disponível",6:"disponível",7:"disponível",8:"disponível",
9:"disponível",10:"disponível",13:"disponível",14:"disponível",15:"disponível",16:"disponível",
17:"disponível",20:"disponível",21:"disponível",22:"disponível",23:"disponível",24:"disponível",
27:"disponível",28:"disponível",29:"disponível",30:"disponível"}

labs = {"Informatica 1":"disponível","Informatica 2":"disponível","Saude 1":"disponível","Saude 2":"disponível",
"Sala reunião":"disponível","Aula":"disponível"}

login = input("Insira seu nome para login: ")
senha = input("Insira sua senha: ")

#menu
while True:
    print("")
    print(f"Bem vindo {login}! \n 1-Agendar \n 2-Ver meus agendamentos \n 3-Sair")
    escolha = int(input(""))
    print("")
    #opções de menu
    if escolha == 1:
        #mostrando labs disponiveis
        for x,y in labs.items():
                print(x,y)
        #escolhendo lab
        print("")
        labEscolhido = input("Escolha o lab que deseja agendar: ")
        print("")
        #mostrando os dias disponiveis
        for x,y in dias.items():
                print(x,y)
        print("")
        #escolhendo dia
        print("Mês de setembro apenas")
        diaEscolhido = input("Escolha o dia: ")
        print("")
        #mudando disponivel para indisponível na lista de labs
        if labEscolhido in labs:
            labs[labEscolhido] = "Indisponível"
            print("Lab agendado com sucesso")
        else:
            print("Lab inválido")
        #mudando disponivel para indisponível na lista de dias        
        if diaEscolhido in dias:
            dias[diaEscolhido] = "Indisponível"
    #mostrando agendamento        
    elif escolha == 2:
         print("Seus agendamentos são: \n Laboratório:", labEscolhido, "no dia:", diaEscolhido)
        
    #sair do menu    
    elif escolha == 3:
        break
    #opçaõ invalida, caso fuja das 3 opções
    else:
        print("Opção invalida")
        time.sleep(3)
        continue
