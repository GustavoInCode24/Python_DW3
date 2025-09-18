from model.Cliente import Cliente
from model.Filme import Filme

class Locadora:
    def __init__(self):
        self.clientes = []
        self.filmes = []

    def cadastrar_filme(self, filme:Filme):
        with open('filmes.txt', 'a') as arquivoFilmes:
            arquivoFilmes.write(filme.titulo + "," + filme.genero + "," + str(filme.ano) + "," + str(filme.codigo) + "," + str(filme.disponivel) + "\n")

    def cadastrar_cliente(self, cliente:Cliente):
        with open('clientes.txt', 'a') as arquivoClientes:
            arquivoClientes.write(cliente.nome + "," + cliente.cpf + "\n")

    def listar_filmes_disponiveis(self):
        with open('filmes.txt', 'r') as arquivoFilmes:
            for linha in arquivoFilmes:
                campos = linha.strip().split(",")
                if campos[4] == "True":
                    print(campos)
            print("")

    def listar_clientes(self):
        with open('clientes.txt', 'r') as arquivoClientes:
            for linha in arquivoClientes:
                campos = linha.strip().split(",")
                print(campos)
            print("")

    def alugar_filme(self, cpf_cliente, codigo_filme):
        cliente_encontrado = False
        with open("clientes.txt", "r") as arquivoClientes:
            for linha in arquivoClientes:
                campos = linha.strip().split(",")
                if campos[1] == cpf_cliente:
                    print("Cliente encontrado!")
                    cliente_encontrado = True
                    
        if not cliente_encontrado:
            print("Cliente não encontrado!")
            return

        with open("filmes.txt", "r") as arquivoFilmes:
            linhas = arquivoFilmes.readlines()

        with open("filmes.txt", "w") as arquivoFilmesAtualizar:
            for linha in linhas:
                campos = linha.strip().split(",")
                if campos[3] == str(codigo_filme):
                    if campos[4] == "True":
                        campos[4] = "False"
                        print(f"Filme '{campos[0]}' alugado com sucesso!")
                    else:
                        print(f"Filme '{campos[0]}' não disponível")
                arquivoFilmesAtualizar.write(",".join(campos) + "\n")
        
        with open("aluguel.txt", 'a') as arquivoAluguel:
            arquivoAluguel.write(str(cpf_cliente) + "," + str(codigo_filme) + ",emprestado\n")

    def devolver_filme(self, cpf_cliente, codigo_filme):
        cliente_encontrado = False
        with open("clientes.txt", "r") as arquivoClientes:
            for linha in arquivoClientes:
                campos = linha.strip().split(",")
                if campos[1] == cpf_cliente:
                    print("Cliente encontrado!")
                    cliente_encontrado = True
                
        if not cliente_encontrado:
            print("Cliente não encontrado!")
            return

        with open("filmes.txt", "r") as arquivoFilmes:
            linhas = arquivoFilmes.readlines()

        with open("filmes.txt", "w") as arquivoFilmesAtualizar:
            for linha in linhas:
                campos = linha.strip().split(",")
                if campos[3] == str(codigo_filme):
                    if campos[4] == "False":
                        campos[4] = "True"
                        print(f"Filme '{campos[0]}' devolvido com sucesso!")
                    else:
                        print(f"Filme '{campos[0]}' já estava disponível")
                arquivoFilmesAtualizar.write(",".join(campos) + "\n")

        with open("aluguel.txt", "a") as arquivoAluguel:
            arquivoAluguel.write(str(cpf_cliente) + "," + str(codigo_filme) + ",devolvido\n")
