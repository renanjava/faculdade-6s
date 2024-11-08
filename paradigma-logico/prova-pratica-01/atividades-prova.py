from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, A, B, Experiente, Funcionario, Departamento, Alocacao, Projeto, TrabalhaEm, PertenceAoDepartamento')

with open("departamentos.txt", "r") as arquivo: 
    for linha in arquivo: 
        lista = linha.strip().split(";") 
        +Departamento(lista[0], lista[1])

with open("funcionarios.txt", "r") as arquivo: 
    for linha in arquivo: 
        lista = linha.strip().split(";") 
        +Funcionario(lista[0], lista[1], lista[2])

with open("projetos.txt", "r") as arquivo: 
    for linha in arquivo: 
        lista = linha.strip().split(";") 
        +Projeto(lista[0], lista[1])

#01
    #É os próprios predicatos

#02
TrabalhaEm(X, A) <= Funcionario(X, Y, Z) & Projeto(A, Y)
PertenceAoDepartamento(X, Y) <= Funcionario(X, Y, Z) & Departamento(Y, B)

#03
Experiente(X, Z) <= Funcionario(X, Y, Z) & (Z >= "5")

#========================================================================================

#01
print("\n\n")
print("Lista dos departamentos: \n", Departamento(X, Y))
print("\n\n")
print("Lista dos funcionários: \n", Funcionario(X, Y, Z))
print("\n\n")
print("Lista dos projetos: \n", Projeto(X, Y))
print("\n\n")

#02
print("\n\n")
print("Todos os funcionários com seus projetos e departamentos respectivos.", TrabalhaEm(X, A) & PertenceAoDepartamento(X, Y))
print("\n\n")

#03
print("\n\n")
print("Todos os funcionários: \n", Funcionario( X, Y, Z))
print("\n\n")
print("Funcionários experientes: \n", Experiente(X, Z))
print("\n\n")