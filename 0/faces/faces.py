def convert(arg1):
    emoji = arg1
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    return emoji
def main():
    userinput = input("Hi, how are you? ")
    userinput = convert(userinput)
    print(userinput)

main()

