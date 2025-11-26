astronauta = input("Nome do astronauta: ")
sup = ["Comida", "Agua", "Oxigênio", "Roupas", "Equipamento"]
peso = [250, 100, 300, 150, 300]

#Cargas
carga_max = 1000
carga_atual = 0

print(astronauta)


i = 1
for item in sup:
    print(i, "-", item)
    i+=1

while True:
    escolha_sup = input("Escolha seus suprimentos: ")

    if escolha_sup.lower() == 'fim':
        break

    if escolha_sup.isdigit():
        escolha_sup = int(escolha_sup)
        if escolha_sup >= 1 and escolha_sup <= 5:
            indice = escolha_sup - 1
            if carga_atual + peso[indice] <= carga_max:
                carga_atual += peso[indice]
                print("Levando ",sup[indice]," - Peso: ",peso[indice],"kg.")
            else:
                print("Não há espaço suficiente para carregar este suprimento!")
        else:
            print("Escolha inválida")
    else:
        print("Entrada inválida. Digite um número de 1 a 5 ou 'Fim' para encerrar.")

espaco_sobra = carga_max - carga_atual

print("\nAstronauta: ",astronauta)
print("Carga: ",carga_atual)
print("Espaço restante: ", espaco_sobra)
