"""
camelCase = input("camelCase: ") #name firstName preferredFirstName
snakeCase = {
    "name": "name",
    "firstName": "first_name",
    "preferredFirstName": "preferred_first_name"
}

if camelCase in snakeCase:
    print(snakeCase[camelCase])
"""

'''
camelCase = input("Insert camelCase: ")
snake = ""

for c in camelCase:
    if c.isupper():
        c = "_" + c.lower()
        snake += c
    else:
        snake += c
print(snake)
'''

camelCase = input("camelCase: ").strip()
camelCase = camelCase[0].lower() + camelCase[1:]

for cha in camelCase:
    if cha.isupper():
        print("_" + cha.lower(), end="")
    else:
        print(cha, end="")
print()


