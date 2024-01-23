"""
deepq = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

if deepq == "42" or deepq == "forty-two" or deepq =="forty two":
    print("Yes")
else:
    print("No")

"""
deepq = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
deepq = deepq.strip()
deepq = deepq.lower()

match deepq:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")


