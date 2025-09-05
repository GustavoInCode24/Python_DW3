from Funcionario import Funcionario
from Comissionado import Comissionado

print("--Funcionario Comum--")

codigo = input("Digite o codigo do funcionario: ")
nome = input("DIgite o nome do funcionario: ")
valorhora = float(input("Digite os valores das horas trabalhadas: R$ "))
horastrabalhadas = float( input("Digite as horas trabalhadas: ") )

FuncionarioComum = Funcionario (codigo, nome, valorhora, horastrabalhadas)

FuncionarioComum.exibirFuncionario()

print("=========================================")

print("--Funcionario Comissionario--")

codigo = input("Digite o codigo do funcionario: ")
nome = input("Digite o nome do funcionario: ")
valorhora = float(input("Digite os valores das horas trabalhadas: R$ "))
horastrabalhadas = float(input("Digite as horas trabalhadas: "))
vendas = float(input("Digite sua quantidade de vendas: R$ "))

   
Funcionario_Comissionario = Comissionado(codigo, nome, valorhora, horastrabalhadas, vendas)
Funcionario_Comissionario.exibirComissionario()
