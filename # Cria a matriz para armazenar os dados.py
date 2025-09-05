alunos = []

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append([nome, nota])

soma_notas = sum([aluno[1] for aluno in alunos])
media_geral = soma_notas / len(alunos)

print("\nNotas dos alunos:")
for aluno in alunos:
    print(f"{aluno[0]}: {aluno[1]}")

print(f"\nMédia geral da turma: {media_geral:.2f}")