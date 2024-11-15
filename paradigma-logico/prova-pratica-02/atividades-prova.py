from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, A, B, C, P, D, Funcionario, ColegaProjeto, ProjetoCompartilhado, Projeto, DepartamentoLotado, Departamento, Funcionario')

with open("funcionarios.txt", "r") as arquivo: 
    for linha in arquivo: 
        lista = linha.strip().split(";") 
        +Funcionario(lista[0], lista[1], lista[2])

with open('projetos.txt', 'r') as arquivo:
    for linha in arquivo:
        lista = linha.strip().split(';')
        +Projeto(lista[0], lista[1])

with open("departamentos.txt", "r") as arquivo: 
    for linha in arquivo: 
        lista = linha.strip().split(";") 
        +Departamento(lista[0], lista[1])

# 06
ColegaProjeto(X, A, Y) <= Funcionario(X, Y, Z) & Funcionario(A, B, C) & (Y == B) & (X != A)

# 06
print(ColegaProjeto(X, Y, Z))

# 05
ProjetoCompartilhado(P) <= Projeto(P, X) & Funcionario(A, X, B)
Funcionario(A, X) <= ProjetoCompartilhado(P) & Funcionario(A, X, B)

# 05
print(ProjetoCompartilhado(P))
print(Funcionario(A, X))

# 04
departamentoLotado = {
    "Planejamento": 0,
    "Vendas Internacionais": 0,
    "Engenharia": 0,
    "Compliance": 0,
    "Legal": 0,
    "Operações": 0,
    "Infraestrutura": 0,
    "Qualidade": 0,
    "Suporte": 0,
    "TI": 0,
    "Vendas": 0,
    "Financeiro": 0,
    "Recursos Humanos": 0,
    "Marketing": 0,
    "Desenvolvimento": 0,
}

for funcionario in Funcionario(X, Y, Z):
    if(funcionario[1] == 'Departamento'):
        continue
    departamentoLotado[str(funcionario[1])] += 1

DepartamentoLotado(D) <= Departamento(D, A) & Funcionario(X, Y, Z) & (departamentoLotado[str(D)] >= A)

# 04
print(DepartamentoLotado(D))