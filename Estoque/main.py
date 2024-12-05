#Cire um estoque e permita que o user mude
#remova produto
#mude quantiade
#add qnt entrada
#add qts saida
#Deifinir funções para usuarios diferentes


#user
# users = []
# user = input("Digite seu nome: ")
# users.append(user)   
    #Verificando usuario


"""
    #quantos produtos vai colocar 
qtd_produtos = int(input("Digite quantos produtos será colocado: "))
    #Criando estoque  
estoque = []

    #Add produtos ao estoque
for produto in range(qtd_produtos):
    linha = []

    #Pedindo tudo que precisa 
    for posição in range(1):
        produto = input(f"Digite o produto: ")
        entrada = int(input(f"Digite quantos {produto} entraram: "))
        saida = int(input(f"Digite quantos {produto} sairam: "))
        linha.append(produto)
        linha.append(entrada)
        linha.append(saida)
    estoque.append(linha) #colando tudo no estoque

    #Criando estoque  
estoque = [
    ["Capa", 10, 5]
    ["Capa space", 10, 6 ]
]
    #Mostrando a estoque
for linha in estoque:
    print("Estoque:")
    print(f"Produtos: {linha [0]} Entrada: {linha [1]} -- Saida: {linha [2]}")

opções =print("\nMudança possiveis: \n 1.Excluir produto \n 2.Mudar quantidade de Entrada \n 3.Mudar quantidade de Saida ")
escolha = int(input("\nDigite a opção desejada: "))

#---------------------------------------------------
##OPÇÕES 1

if escolha == 1:
    #Localizando opção
    print("Produtos:")
    for linha in estoque:
        print(linha [0])

    #Escolhendo produto para excluir
    produto_excluir = input("Digite o produto que quer excluir: ").capitalize()
    
    #Excluindo produto
    for linha in estoque:
        if linha[0] == produto_excluir:
            estoque.remove(linha)
        if produto_excluir == "parar":
             break

    #Mostrando o Estoque atualizado separado por linhas
    for linha in estoque:
        print(linha)

#-----------------------------------------------------------------
##OPÇÃO 2 

elif opções == 2:
    #Localizar opção
    print("Produtos:")
    for linha in estoque:
        if escolha == 2:
            print(linha [0], linha[1])

    #Escolhendo produto para mudar a qnt entrada
    produto_entrada = input("Digite o nome produto, para mudar a qtd entrada: ").capitalize()

    #Add qtd entrada
    for linha[1] in estoque:
        nova__entrada = int(input("Digite o novo valor a ser somado: "))
        nova_entrada = entrada
        linha.append( )

    # for 




    #Localizar opção
print("Produtos:")
for linha in estoque:
    if escolha == 3:
        print(linha [0], linha[2])
"""