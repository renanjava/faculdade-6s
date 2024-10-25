from pyDatalog import pyDatalog


pyDatalog.create_terms('e, equipe, tecnologia, comunicacao, trabalha_com, X, Y')

+e('Alice', 'Desenvolvimento')
+e('Bob', 'Desenvolvimento')
+e('Carol', 'Marketing')
+e('David', 'Marketing')
+e('Eve', 'Design')

+trabalha_com('Alice', 'tecnologia')
+trabalha_com('Bob', 'tecnologia')
+trabalha_com('Eve', 'tecnologia')
+trabalha_com('Carol', 'comunicacao')
+trabalha_com('David', 'comunicacao')

pyDatalog.assertd((trabalha_com(X, 'tecnologia') <= e(X, 'Desenvolvimento')))
pyDatalog.assertd((trabalha_com(X, 'tecnologia') <= e(X, 'Design')))
pyDatalog.assertd((trabalha_com(X, 'comunicacao') <= e(X, 'Marketing')))

print("Pessoas que trabalham com tecnologia:")
for (pessoa,) in pyDatalog.ask((X, 'trabalha_com', X, 'tecnologia')).answers:
    print(pessoa)

carol_comunicacao = pyDatalog.ask(('Carol', 'trabalha_com', 'Carol', 'comunicacao'))
print("\nCarol trabalha com comunicação?", bool(carol_comunicacao))

print("\nPessoas e seus tipos de trabalho:")
for (pessoa, trabalho) in pyDatalog.ask((X, Y, 'trabalha_com', X, Y)).answers:
    print(f"{pessoa} trabalha com {trabalho}")
