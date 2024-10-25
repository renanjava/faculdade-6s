from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, gosta_de, em_comum')

with open("esportes.txt", "r") as arquivo:
	esportes = arquivo.read()

arrayEsportes = esportes.split("\n")

for esportes_info in arrayEsportes:
    if esportes_info.strip():
        nome, esporte = esportes_info.split()
        +gosta_de(nome, esporte)

em_comum(X, Y, Z) <= gosta_de(X, Z) & gosta_de(Y, Z) & (X < Y)
print(em_comum(X, Y, Z))