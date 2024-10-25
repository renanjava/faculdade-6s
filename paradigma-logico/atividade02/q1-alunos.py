from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, aluno, aprovado')

with open("alunos.txt", "r") as arquivo:
	alunos = arquivo.read()

arrayAlunos = alunos.split("\n")

for aluno_info in arrayAlunos:
    if aluno_info.strip(): 
        nome, nota = aluno_info.split()
        +aluno(nome, nota)

aprovado(X)<= aluno(X, Y) & (Y >= '7.0')

print(aprovado(X))