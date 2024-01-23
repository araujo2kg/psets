greet = input("Greetings good sir: ")
greet = greet.lower().lstrip()


if greet.find("hello") == 0:
    print("$0")
elif greet.find("h") == 0:
    print("$20")
else:
    print("$100")
