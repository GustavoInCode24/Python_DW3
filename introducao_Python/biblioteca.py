ultimo_id = 0

print ("\n---Biblioteca---")

print("Quando terminar digitar 'sair' \n")

while True:
    
    autor = input("Digite o nome do autor: ")
    
    if autor == 'sair':
        break

    titulo= input("Digite o titulo do livro: ")

    ultimo_id += 1

    with open ('livros.txt','a') as arquivo:
   
        arquivo.write(str(ultimo_id))
        arquivo.write("; ")
        arquivo.write(titulo)
        arquivo.write("; ")
        arquivo.write(autor)
        arquivo.write(";")
        arquivo.write("\n")

print("\n---Exibindo Livros---")
    
with open('livros.txt','r') as arquivo:
    for linha in arquivo:
        lista = linha.strip()
        print(lista)

print("\n---Livros Buscados---")

buscar_livro = input("Digite o autor ou o livro que deseja buscar:")

encontrado = False

with open('livros.txt','r') as arquivo:
    for linha in arquivo:
        if not linha.strip():
            continue

        partes = linha.strip().split(";")
        
        if len(partes) >= 3:
            id_livro, titulo, autor = partes[0], partes[1], partes[2]
            
            if buscar_livro.lower() in autor.lower() or buscar_livro.lower() in titulo.lower():
                print(f"Livro encontrado: {titulo} - {autor}")
                encontrado = True
                

    if not encontrado:
        print("Livro não encontrado.")



