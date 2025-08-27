contato = {
 
}
 
while True:
    
    print("\n---Adicinando contatos---") 
       
    nome = input("Digite seu nome (digite 'sair' para sair): ")
 
    if nome == "sair":
        break
 
    telefone = input("Digite seu telefone: ")
       
    if telefone in contato.values():
        contato.update({nome : telefone})
        
    else:
            contato[nome] = telefone
           
while True:
    
    print("\n---Busacando Contatos---")
    
    nomebuscado = input("Digite o nome que deseja buscar (digite 'sair' para sair ): ")

    if nomebuscado == "sair":
        break
    
    if nomebuscado in contato:
        telefone_encontrado = contato[nomebuscado]
        print(f"Telefone de {nomebuscado}: {telefone_encontrado}")
            
    else:  
         print(f"Contato '{nome_buscado}' não encontrado.")
        
while True:
    
    print("\n---Excluir Contato---")

    contatoExcluir = input("Digite o nome do contato a ser excluido:  (digite 'sair' para sair): ")
        
    if contatoExcluir == "sair":
        break    
    
    if contatoExcluir in contato:
        del contato[contatoExcluir]
        print("Contato removido")
        
    else:
        print("Esse contato não existe")
        
         
        