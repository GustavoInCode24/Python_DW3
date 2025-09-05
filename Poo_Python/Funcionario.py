class Funcionario:
    def __init__(self, codigo, nome , valorhora, horastrabalhadas):
        self.codigo = codigo
        self.nome = nome
        self.valorhora = valorhora
        self.horastrabalhadas = horastrabalhadas
        self.salario = self.calcularSalario()


    def calcularSalario(self):
        return self.valorhora * self.horastrabalhadas    
    
    def exibirFuncionario(self):
        
        print( f"Código: {self.codigo} ,Nome: {self.nome}, Salario: {self.salario:.2f} "  )
