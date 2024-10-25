from pyDatalog import pyDatalog

pyDatalog.create_terms('animal, carnívoro, herbívoro, come, selvagem, X, Y')

+carnívoro('Tigre')
+carnívoro('Leão')
+carnívoro('Urso')

+herbívoro('Girafa')
+herbívoro('Elefante')
+herbívoro('Zebra')

+come(X, 'carne') <= carnívoro(X)

+come(X, 'plantas') <= herbívoro(X)

+selvagem(X) <= carnívoro(X)
+selvagem(X) <= herbívoro(X)

tem_herbivoro = pyDatalog.ask((X, 'come', X, 'plantas'))
print("Existe algum animal que come plantas?", bool(tem_herbivoro))

print("\nAnimais selvagens:")
for (animal,) in pyDatalog.ask((X, 'selvagem', X)).answers:
    print(animal)

todos_carnivoros_selvagens = pyDatalog.ask((X, 'selvagem', X) <= (carnívoro(X)))
print("\nTodos os carnívoros são selvagens?", bool(todos_carnivoros_selvagens))
