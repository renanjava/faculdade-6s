import sqlite3
from pyDatalog import pyDatalog

conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

pyDatalog.create_terms('X, Y, faz_pedido, cliente, pedido')

for row in cursor.execute('SELECT * FROM clientes'):
    (cliente(row[0]), pedido(row[0], row[1]))

conn.close()

faz_pedido(X, Y) <= (cliente(X), pedido(X, Y))

print(X, faz_pedido(X, 'Livro'))