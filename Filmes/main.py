#Situação Problema:

#Você faz parte de uma equipe de desenvolvedores encarregada de
#criar um sistema simples para gerenciar filmes em um catálogo. Esse
#sistema deve permitir o cadastro, visualização, atualização e
#exclusão de informações de filmes. Sua tarefa é criar uma solução
#que implemente essas funcionalidades utilizando listas/matriz em
#Python para armazenar os dados.

#Requisitos:
#1. Cadastrar Filmes:• Adicionar filmes ao sistema, incluindo Título, Gênero e Ano de Lançamento.
#2. Listar Filmes: • Exibir todos os filmes cadastrados, mostrando seus dados organizados em colunas.
#3. Buscar por Gênero: • Exibir todos os filmes cadastrados de um gênero específico informado pelo usuário.
#4. Excluir Filme: • Remover filmes cadastrados com base em sua posição na lista.

import time
# time.sleep(2)

#Lista de Filmes
filmes = [
    ["Alvin", "Terror", "2018"],
    ["Cleber", "Drama", "2000"],
]

#nome user
nome_user= input("Digite seu nome: ")

while True:

    #Opções do user
    print(" -"*30,"\n Escolha uma opção:\n","-"*30)
    print(" 1. Cadastras filme\n 2. Lista de filme\n 3. Buscar\n 4. Excluir\n 5. Sair\n","-"*30)

    #Escolha do user
    escolha = int(input(f"Digite uma opção {nome_user} (numero): "))

    ## Opção 1
    #cadastras filme
    if escolha == 1:
        qtd_filmes = int(input(f"Quantos Filmes deseja cadastrar {nome_user}: "))
        time.sleep(2)

        for novo in range(qtd_filmes):
            novos = []
            for num in range(1):
                novo_filme = input(f"Qual filme deseja cadastrar {nome_user}(filme de numero {novo+1}): ").capitalize()
                genero= input(f"Qual genero do filme {novo_filme}: ").capitalize()
                data= input(f"Qual data de lançamento do filme {novo_filme}: ")
                novos.append(novo_filme)
                novos.append(genero)
                novos.append(data)
            filmes.append(novos)

    #Lista de filmes atualizada
        print("\nLista de todos os filmes: ")
        for novos in filmes:
            print(f"FILME: {novos[0]}")
        time.sleep(3)

    ##Opção 2
    #Listar Filmes
    elif escolha == 2:
        print("\nLista de todos os filmes: ")
        for novos in filmes:
            print(f"Filme: {novos[0]} Gênero: {novos[1]} Lançamento: {novos[2]}")
        else:
            print(f"Cadastre agora um filme {nome_user}!!")   
        time.sleep(3)

    ##Opção 3
    #Listar buscar por genero
    elif escolha == 3:
        #Nome do genero
        nome_genero = input(f"Qual gênero deseja buscar {nome_user}: ").capitalize()
        
        #Buscando filme
        print(f"Todos os filmes do gênero: {nome_genero}")
        lista_erro = []
        for genero in filmes:
            if genero[1] == nome_genero:
                print(genero[0])
                if genero[1] != nome_genero:
                    lista_erro.append(nome_genero)
                print("Gênero não encontrado ")
        time.sleep(3)

    ##Opção 4
    #Excluir Filme
    elif escolha == 4:
        #Lista dos filmes
        print("\nLista de todos os filmes: ")
        for novos in filmes:
            print(novos)

        #Escolhendo filme
        excluir_filme= input(f"\nQual filme deseja excluir {nome_user}: ").capitalize()
        time.sleep(2)

        #Excluindo filme
        for filme in filmes:
            if filme[0] == excluir_filme:
                print(filme[0])
                filmes.remove(filme)
    
        time.sleep(3)
        
        #Nova lista dos filmes
        print(f"\nLista de todos os filmes feita para você {nome_user}: ")
        for novos in filmes:
            print(novos)
        time.sleep(3)

        ##OPÇÂO 5
        #Sair
    elif escolha == 5:
        print(f"Até Breve {nome_user} !!")
        break

        

    
    