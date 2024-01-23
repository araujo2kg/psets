vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def main():
    inp = input("Insert here to shorten: ")
    print(shorten(inp))

def shorten(word):
    full = ""
    for cha in word:
        if cha not in vowels:
            full = full + cha
    return full


if __name__ == "__main__":
    main()
