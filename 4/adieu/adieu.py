import inflect

p = inflect.engine()
names = []


def get_name():
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            return names


name_list = get_name()
print("Adieu, adieu, to", p.join(name_list))
