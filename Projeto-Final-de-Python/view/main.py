import os
from controller.Locadora import Locadora
from model.Cliente import Cliente
from model.Filme import Filme

locadora = Locadora()
os.system("cls")

while True:
    print("[1] - Cadastrar cliente")
    print("[2] - Cadastrar filme")
    print("[3] - Listar clientes")
    print("[4] - Listar filmes disponíveis")
    print("[5] - Alugar filme")
    print("[6] - Devolver filme")
    print("[0] - Sair")

    escolha = int(input("Escolha uma opção: "))
    os.system("cls")

    if escolha == 1:
        nome = input("Insira o nome do cliente: ")
        cpf = input("Insira o CPF do cliente: ")
        cliente = Cliente(nome, cpf)
        locadora.cadastrar_cliente(cliente)
        print("Cliente cadastrado com sucesso!\n")

    elif escolha == 2:
        titulo = input("Insira o título do filme: ")
        genero = input("Insira o gênero do filme: ")
        ano = int(input("Insira o ano do filme: "))
        codigo = input("Insira o código do filme: ")
        filme = Filme(titulo, genero, ano, codigo, True)
        locadora.cadastrar_filme(filme)
        print("Filme cadastrado com sucesso!\n")

    elif escolha == 3:
        print("Clientes cadastrados:")
        locadora.listar_clientes()
        input("Pressione Enter para continuar...")
        os.system("cls")

    elif escolha == 4:
        print("Filmes disponíveis:")
        locadora.listar_filmes_disponiveis()
        input("Pressione Enter para continuar...")
        os.system("cls")

    elif escolha == 5:
        cpf = input("Insira o CPF do cliente: ")
        codigo = input("Insira o código do filme: ")
        locadora.alugar_filme(cpf, codigo)
        input("Pressione Enter para continuar...")
        os.system("cls")

    elif escolha == 6:
        cpf = input("Insira o CPF do cliente: ")
        codigo = input("Insira o código do filme: ")
        locadora.devolver_filme(cpf, codigo)
        input("Pressione Enter para continuar...")
        os.system("cls")

    elif escolha == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        input("Pressione Enter para continuar...")
        os.system("cls")
