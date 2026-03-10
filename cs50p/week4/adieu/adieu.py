import inflect


p = inflect.engine()

names = []
while True:
    try:
        name = input().strip()
        names.append(name)
    except EOFError:
        break

sep_names = p.join(names)
print('Adieu, adieu, to ' + sep_names)
