class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nota: {self.nota}")

aluno1 = Aluno("Lucas", 17, 8.5)
aluno1.exibir_dados()