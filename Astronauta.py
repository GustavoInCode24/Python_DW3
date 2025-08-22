def main():
  
    capacidade_max = 1000
    carga_atual = 0

    suprimentos = {
        "comida": 200,
        "água": 100,
        "oxigênio": 300,
        "ferramentas": 250,
        "remédios": 150
    }

   
    nome = input("Digite o nome do astronauta: ")

    print("\n--- Lista de suprimentos disponíveis ---")
    for item, peso in suprimentos.items():
        print(f"- {item.capitalize()} ({peso} kg)")
    print("---------------------------------------\n")


    while True:
        escolha = input("Escolha um suprimento (ou digite 'fim' para encerrar): ").lower()

        if escolha == "fim":
            break

        if escolha in suprimentos:
            peso_item = suprimentos[escolha]

            # Verifica se ainda cabe na nave
            if carga_atual + peso_item <= capacidade_max:
                carga_atual += peso_item
                print(f"{escolha.capitalize()} adicionado! Carga atual: {carga_atual} kg")
            else:
                print(f" Não há espaço suficiente para adicionar {escolha}!")
        else:
            print(" Suprimento inválido! Escolha um da lista.")

  
    espaco_restante = capacidade_max - carga_atual


    print("\n--- Resumo da Missão ---")
    print(f"Astronauta: {nome}")
    print(f"Carga utilizada: {carga_atual} kg")
    print(f"Espaço restante: {espaco_restante} kg")
    print("-------------------------")



if __name__ == "__main__":
    main()
