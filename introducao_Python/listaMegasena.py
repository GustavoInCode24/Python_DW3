import random

lista = random.sample(range(1, 11), 6)
listajogador= []
acertos =0
numero_acertados =[]

print("Escolha de 6 a 20 números entre 1 e 10.")

while len(listajogador)< 20:

    numero = input ("Digite um número (ou 'sair' para encerrar):")

    if numero.lower() == "sair":
        if len(listajogador) >= 6:
            break 
        else:
            print("Você precisa digitar pelo menos 6 números.")
        continue
    numero =  int(numero)

    listajogador.append(numero)


print("\n--Seus numeros:", listajogador)
print("\n--Numeros jogados:",lista)


for numero in listajogador:
    if numero in lista:
        acertos += 1
        numero_acertados.append(numero)



if acertos == 6:
    print("Você acertou a Sena")
elif acertos == 5:
     print("Você acertou uma Quina")
elif acertos == 4:
    print("Você acertou uma Quadra") 
else:
     print("Você não acertou nenhum numero")
if acertos > 0:
    print("Números acertados:", numero_acertados)     








   
     