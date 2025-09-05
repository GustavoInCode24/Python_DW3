from Funcionario import Funcionario

class Comissionado(Funcionario):
    def __init__(self, codigo, nome, valorhora, horastrabalhadas, vendas):
        self.vendas = vendas
        super().__init__(codigo, nome, valorhora, horastrabalhadas)
        

    def calcularSalario(self):
        return (self.valorhora * self.horastrabalhadas) + (self.vendas * 0.15)
    
    def exibirComissionario(self):
       
       print( f"Código: {self.codigo} ,Nome: {self.nome}, Salario: {self.salario} ")