import inflect
names = []
while True:
    try:
        name = input('Name:')
        names.append(name)
    except EOFError:
        break

engine = inflect.engine()
sentence = f'Adieu, adieu, to {engine.join(names)}'
print(sentence)
