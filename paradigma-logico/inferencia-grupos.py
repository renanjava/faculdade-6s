from pyDatalog import pyDatalog

pyDatalog.create_terms('equipe, tecnologia, comunicacao, trabalha_com, X, Y')

pyDatalog.assert_fact('equipe', 'Alice', 'Desenvolvimento')
pyDatalog.assert_fact('equipe', 'Bob', 'Desenvolvimento')
pyDatalog.assert_fact('equipe', 'Carol', 'Marketing')
pyDatalog.assert_fact('equipe', 'David', 'Marketing')
pyDatalog.assert_fact('equipe', 'Eve', 'Design')

pyDatalog.assert_fact('trabalha_com', 'Alice', 'tecnologia')
pyDatalog.assert_fact('trabalha_com', 'Bob', 'tecnologia')
pyDatalog.assert_fact('trabalha_com', 'Eve', 'tecnologia')
pyDatalog.assert_fact('trabalha_com', 'Carol', 'comunicacao')
pyDatalog.assert_fact('trabalha_com', 'David', 'comunicacao')

print("Pessoas que trabalham com tecnologia:")
for (pessoa,) in pyDatalog.ask((X, 'trabalha_com', X, 'tecnologia')).answers:
    print(pessoa)

carol_comunicacao = pyDatalog.ask(('Carol', 'trabalha_com', 'Carol', 'comunicacao'))
print("\nCarol trabalha com comunicação?", bool(carol_comunicacao))

print("\nPessoas e seus tipos de trabalho:")
for (pessoa, trabalho) in pyDatalog.ask((X, Y, 'trabalha_com', X, Y)).answers:
    print(f"{pessoa} trabalha com {trabalho}")
