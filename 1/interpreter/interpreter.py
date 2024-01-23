def oper(n, n2, n3):
        if n2 == "+":
         return (n + n3)
        elif n2 == "-":
         return (n - n3)
        elif n2 == "*":
            return (n * n3)
        elif n2 == "/":
            return (n / n3)

math = input("Expression: ").strip()

if "+" in math:
    math = math.partition("+")
elif "-" in math:
    math = math.partition("-")
elif "*" in math:
    math = math.partition("*")
elif "/" in math:
    math = math.partition("/")
else:
    print("We don't support this operation :(")
    exit()

x = int(math[0])
y = math[1]
z = int(math[2])

result = float(oper(x, y, z))

print(f"{result:.1f}")



